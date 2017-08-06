# =============================================================================
# >> IMPORTS
# =============================================================================
# Python
import asyncio
from base64 import b64encode
from hashlib import sha256
import json

# websockets
import websockets

# obs-ws-rc
from .events import events
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
    pass


class OBSWS:
    def __init__(self, host, port=DEFAULT_PORT, password=None, skip_auth=False,
                 **kwargs):

        """Create OBSWS instance.

        :param str host: Server host
        :param int port: Server port
        :param str or None password: Server password (if needed)
        :param bool skip_auth: Whether or not to perform authentication
        :param asyncio.AbstractEventLoop loop: Event loop to use (can only be
            passed explicitly as a keyword argument)
        """
        if 'loop' not in kwargs:
            raise TypeError(
                "{class_name}() missing a required keyword argument: "
                "'loop'".format(class_name=self.__class__.__name__))

        self._loop = kwargs['loop']
        self._host = host
        self._port = port
        self._password = password
        self._skip_auth = skip_auth

        self._message_map = {}
        self._message_count = 0

        self._event_handlers = {}

        self._ws = None
        self._ws_closed_future = None

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
        :rtype: str or None

        """
        return self._password

    async def __aenter__(self):
        """Establish connection to the server, start the event loop and
        perform authentication (the latter can be skipped with ``skip_auth``
        argument in :meth:`__init__`)

        :return: Ready-to-work OBSWS instance
        :rtype: OBSWS

        """
        self._ws = await websockets.connect(URI_TEMPLATE.format(
            host=self._host,
            port=self._port
        ))

        asyncio.ensure_future(self._recv_loop())

        if not self._skip_auth:
            await self._authenticate()

        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Close underlying websocket connection, don't suppress the exception.

        """
        await self._ws.close()
        self._ws = None

    async def _recv_loop(self):
        while True:
            try:
                data = json.loads(await self._ws.recv())
            except websockets.ConnectionClosed:
                if self._ws_closed_future is not None:
                    self._ws_closed_future.set_result(None)

                return

            message_id = data.get('message-id')
            if message_id is not None:
                self._message_map.pop(message_id).set_result(data)
                continue

            type_name = data.get('update-type')
            if type_name is not None:
                asyncio.ensure_future(self._handle_event(type_name, data))
                continue

            # TODO: Not a response nor an event - log an error maybe?

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
        :return: Response from the server
        :rtype: requests.BaseResponse

        """
        self._message_count += 1
        message_id = str(self._message_count)
        future = self._message_map[message_id] = self._loop.create_future()

        data = request.get_request_data(message_id)
        await self._ws.send(json.dumps(data))

        response = request.response_class(await future)
        return response

    async def _handle_event(self, type_name, data):
        event_class = events.get(type_name)

        # Do we know of this event type?
        if event_class is None:

            # Not implemented in our protocol, no further action required
            return

        callbacks = self._event_handlers.get(type_name)

        # Is there anybody willing to handle it?
        if callbacks is None:

            # No, so we don't even instantiate the event class
            return

        event = event_class(data)

        futures = []
        for callback in callbacks:
            if asyncio.iscoroutinefunction(callback):
                futures.append(callback(self, event))
            else:
                callback(self, event)

        for future in asyncio.as_completed(futures):
            await future

    def register_event_handler(self, type_name, callback):
        """Register event handler (either a regular one or an async-coroutine).

        :param type_name: Event name
        :param callable callback: Function or coroutine function

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

        """
        self._event_handlers[type_name].remove(callback)
        if not self._event_handlers[type_name]:
            del self._event_handlers[type_name]

    def sock_closed(self):
        """Create and return an awaitable future that completes when the
        underlying socket closes.

        Call this if you want to keep the loop running as long as the
        connection is alive.

        :return: Awaitable future
        :rtype: asyncio.Future

        """
        if self._ws_closed_future is not None:
            raise ValueError("sock_closed() can only be called once")

        self._ws_closed_future = self._loop.create_future()
        return self._ws_closed_future
