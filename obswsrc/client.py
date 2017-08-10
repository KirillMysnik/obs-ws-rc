# =============================================================================
# >> IMPORTS
# =============================================================================
# Python
import asyncio
from base64 import b64encode
from hashlib import sha256
import json
from traceback import format_exc

# websockets
import websockets

# obs-ws-rc
from .events import events
from .logs import logger
from .requests import (
    AuthenticateRequest, GetAuthRequiredRequest, ResponseStatus)


# =============================================================================
# >> CONSTANTS
# =============================================================================
URI_TEMPLATE = "ws://{host}:{port}/"
DEFAULT_PORT = 4444


# =============================================================================
# >> CLASSES
# =============================================================================
class AuthError(Exception):
    """Raised by :meth:`OBSWS.connect` if authentication has failed."""
    pass


class OBSWS:
    """Main class used for obs-websocket communication. Can be used as a
    context manager (given you use it in ``async with`` statement).

    Example usage::

        async with OBSWS("localhost") as obsws:
            ...

    This is an equivalent to the following::

        obsws = OBSWS("localhost")
        await obsws.connect()

        try:
            ...
        finally:
            await obsws.close()

    This class also supports Future-like protocol (it implements
    :meth:`__await__` method). You can await for the OBSWS instance for it
    to close::

        await obsws

    .. note::
        When entering the context manager (using ``async with`` statement),
        you should be ready to except :exc:`AuthError` that might raise due to
        failed auth, or :exc:`OSError` that can be raised by the underlying
        websockets library in case of being unable to connect to OBS Studio.

    .. seealso::
        :meth:`connect`
        :meth:`close`

    """
    def __init__(self, host, port=DEFAULT_PORT, password=None, *,
                 skip_auth=False, loop=None):

        """
        :param str host: Server host
        :param int port: Server port
        :param str|None password: Server password (if needed)
        :param bool skip_auth: Whether or not to skip authentication
        :param asyncio.AbstractEventLoop|None loop: Event loop to use

        """
        self._host = host
        self._port = port
        self._password = password
        self._skip_auth = skip_auth

        if loop is None:
            loop = asyncio.get_event_loop()

        self._loop = loop

        self._message_map = {}
        self._message_count = 0

        self._event_handlers = {}

        self._ws = None
        self._ws_close_event = asyncio.Event(loop=self._loop)
        self._done_event = asyncio.Event(loop=self._loop)
        self._done_event.set()
        self._event_futures = {}

    def __await__(self):
        async def coro():
            return await self._done_event.wait()

        return coro().__await__()

    @property
    def host(self):
        """The host that OBSWS was instantiated with (read-only).

        :return: Server host
        :rtype: str

        """
        return self._host

    @property
    def port(self):
        """The port that OBSWS was instantiated with (read-only).

        :return: Server port
        :rtype: int

        """
        return self._port

    @property
    def password(self):
        """The port that OBSWS was instantiated with (read-only).

        :return: Server password (``None`` if not given)
        :rtype: str|None

        """
        return self._password

    @property
    def closed(self):
        """Return whether or not this OBSWS instance is closed."""
        return self._done_event.is_set()

    async def connect(self):
        """Establish connection to the server, start the event loop and
        perform authentication (the latter can be skipped with ``skip_auth``
        argument in :meth:`__init__`).

        :raises ValueError: if already connected
        :raises AuthError: if auth is enabled but password is invalid or not
                           not set
        :raises OSError: raised by the underlying websockets library if
                         connection attempt is failed

        .. note::
            This method is a coroutine.

        """
        if self._ws is not None:
            raise ValueError("Already connected")

        self._ws = await websockets.connect(URI_TEMPLATE.format(
            host=self._host,
            port=self._port
        ))
        self._ws_close_event.clear()

        asyncio.ensure_future(self._recv_loop())

        if not self._skip_auth:
            try:
                await self._authenticate()
            except AuthError:
                await self._close()
                await self._done_event.wait()
                raise

    async def _close(self):
        """Close the underlying websocket connection.

        .. note::
            This method is a coroutine.

        """
        if self._ws is None:
            return

        try:
            await self._ws.close()
        except ConnectionResetError:
            pass

        self._ws = None
        self._ws_close_event.set()

        for future in self._message_map.values():
            future.set_result(None)

        for future in list(self._event_futures.values()):
            future.set_result(None)

        self._message_map.clear()

    async def close(self):
        """Clean shutdown. Consequent calls on an already closed instance have
        not effect.

        .. note::
            This method is a coroutine.

        """
        await self._close()
        await self._done_event.wait()

    async def __aenter__(self):
        """Enter context: connect and return self.

        :return: Ready-to-work OBSWS instance
        :rtype: OBSWS

        .. note::
            This method is a coroutine.

        """
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Leave context: clean shutdown.

        .. note::
            This method is a coroutine.

        """
        await self._close()
        await self._done_event.wait()

    async def _recv_loop(self):
        self._done_event.clear()

        while not self._ws_close_event.is_set():
            try:
                data = json.loads(await self._ws.recv())
            except websockets.ConnectionClosed:
                await self._close()

            else:
                message_id = data.get('message-id')
                if message_id is not None:
                    self._message_map.pop(message_id).set_result(data)
                    continue

                type_name = data.get('update-type')
                if type_name is not None:
                    asyncio.ensure_future(
                        self._handle_event(type_name, data), loop=self._loop)

                    continue

                # TODO: Not a response nor an event - log an error maybe?

        self._done_event.set()

    async def _authenticate(self):
        response = await self.require(GetAuthRequiredRequest())
        if not response.auth_required:
            return

        if self._password is None:
            raise AuthError(
                "Auth is required, but the password is not provided")

        auth_string = b64encode(sha256(b64encode(
            sha256((self._password + response.salt).encode('utf-8')).digest()
        ) + response.challenge.encode('utf-8')).digest()).decode('ascii')

        response = await self.require(AuthenticateRequest(auth=auth_string))
        if response.status == ResponseStatus.ERROR:
            raise AuthError(
                "Auth has failed, error from the server: '{error}'".format(
                    error=response.error))

    async def require(self, request):
        """Send a request to the server and await, return the response.

        :param requests.BaseRequest request: Fully formed request
        :return: Response from the server (None if the connection was
                 closed during communication)
        :rtype: requests.BaseResponse|None
        :raises ValueError: if not connected

        .. note::
            This method is a coroutine.

        """
        if self._ws is None:
            raise ValueError("Not connected")

        self._message_count += 1
        message_id = str(self._message_count)
        future = self._message_map[message_id] = self._loop.create_future()

        data = request.get_request_data(message_id)
        await self._ws.send(json.dumps(data))

        message = await future
        if message is None:
            return None

        return request.response_class(message)

    def event(self, type_name=None):
        """Return a future that, when awaited for, returns an event of type
        ``type_name``. If ``type_name`` is None, the future result will be the
        first occurred event. If connection is closed while future is not done,
        the future result is None.

        :param str|None type_name: Event type to await for, ``None`` to await
                                   for an event of any type
        :return: Future
        :rtype: asyncio.Future
        :raises ValueError: if not connected

        .. versionchanged:: 2.3.0
           This method is not a coroutine now, but it returns a
           :class:`asyncio.Future` object.

        """
        if self._ws is None:
            raise ValueError("Not connected")

        if type_name not in self._event_futures:
            self._event_futures[type_name] = self._loop.create_future()

            def callback(f):
                del self._event_futures[type_name]

            self._event_futures[type_name].add_done_callback(callback)

        return self._event_futures[type_name]

    async def _handle_event(self, type_name, data):
        event_class = events.get(type_name)

        # Do we know of this event type?
        if event_class is None:

            # Not implemented in our protocol, no further action required
            return

        callbacks = self._event_handlers.get(type_name)
        future_any = self._event_futures.get(None)
        future_event = self._event_futures.get(type_name)

        # Is there anybody willing to handle it?
        if callbacks is None and future_any is None and future_event is None:

            # No, so we don't even instantiate the event class
            return

        try:
            event = event_class(data)
        except:
            logger.error(
                "OBS-WS-RC: '{type_name}' event instantiation raised (invalid "
                "protocol.json?)\n{exc}\nThe callbacks are not going to be "
                "called!".format(type_name=type_name, exc=format_exc()))

            return

        if future_any is not None:
            future_any.set_result(event)

        if future_event is not None:
            future_event.set_result(event)

        if callbacks is not None:
            coros = []
            for callback in callbacks:
                if asyncio.iscoroutinefunction(callback):
                    coros.append(callback(self, event))
                else:
                    try:
                        callback(self, event)
                    except:
                        logger.error(
                            "OBS-WS-RC: '{type_name}' event "
                            "handler raised!\n{exc}\n".format(
                                type_name=type_name, exc=format_exc()))

            close_future = asyncio.ensure_future(self._ws_close_event.wait(),
                                                 loop=self._loop)

            gather_future = asyncio.gather(
                *coros, return_exceptions=True, loop=self._loop)

            done, pending = await asyncio.wait(
                [close_future, gather_future],
                return_when=asyncio.FIRST_COMPLETED,
                loop=self._loop
            )

            if gather_future.done():
                results = await gather_future

                for result in results:
                    if isinstance(result, BaseException):
                        try:
                            raise result
                        except:
                            logger.error(
                                "OBS-WS-RC: '{type_name}' event "
                                "async handler raised!\n{exc}\n".format(
                                    type_name=type_name, exc=format_exc()))

            else:
                gather_future.cancel()

            if not close_future.done():
                close_future.cancel()

    def register_event_handler(self, type_name, callback):
        """Register event handler (either a regular one or an async-coroutine).

        :param type_name: Event name
        :param callable callback: Function or coroutine function
        :raises ValueError: if callback is already registered for the event

        .. deprecated:: 2.2
            Use :meth:`event` instead.

        """
        if type_name not in self._event_handlers:
            self._event_handlers[type_name] = []

        if callback in self._event_handlers[type_name]:
            raise ValueError(
                "Callback '{callback}' is already registered to handle "
                "'{type_name}' event".format(
                    callback=callback, type_name=type_name))

        self._event_handlers[type_name].append(callback)

    def unregister_event_handler(self, type_name, callback):
        """Unregister previously registered event handler.

        :param type_name: Event name
        :param callable callback: Function or coroutine function

        .. deprecated:: 2.2
            Use :meth:`event` instead.

        """
        self._event_handlers[type_name].remove(callback)
        if not self._event_handlers[type_name]:
            del self._event_handlers[type_name]
