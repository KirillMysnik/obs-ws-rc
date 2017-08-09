# =============================================================================
# >> IMPORTS
# =============================================================================
# Python
import asyncio
import logging
import sys
import unittest

# obs-ws-rc
from obswsrc import OBSWS
from obswsrc.client import AuthError
from obswsrc.logs import logger as obwsrc_logger


# =============================================================================
# >> CONSTANTS
# =============================================================================
REF_EVENT = "StreamStatus"
REF_EVENT_AWAITING_TIMEOUT = 5


# =============================================================================
# >> TEST HELPERS
# =============================================================================
def async_test(f):
    def wrapper(self, *args, **kwargs):
        async def run_and_close():
            await f(self, *args, **kwargs)
            await self.obsws.close()

        self.loop.run_until_complete(run_and_close())

    return wrapper


class BaseOBSWSTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.loop = None
        self.obsws = None

    def setUp(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(None)

        self.obsws = OBSWS("localhost", loop=self.loop)

        try:
            self.loop.run_until_complete(self.obsws.connect())

        except OSError:
            self.skipTest(
                "{host}:{port} is unreachable. Is OBS Studio with "
                "obs-websocket plugin launched?".format(
                    host=self.obsws.host, port=self.obsws.port))

        except AuthError:
            self.skipTest(
                "Couldn't auth to obs-websocket. Password: {password}".format(
                    password=self.obsws.password))

    def tearDown(self):
        self.loop.close()
        self.loop = None
        self.obsws = None


class EventNotReceived(Exception):
    pass


async def wait_for_event(obsws, type_name, callback, timeout, *, loop):
    callback_executed = asyncio.Event(loop=loop)

    if asyncio.iscoroutinefunction(callback):
        async def wrapped_callback(obsws, event):
            if not callback_executed.is_set():
                callback_executed.set()

            await callback(obsws, event)

    else:
        def wrapped_callback(obsws, event):
            if not callback_executed.is_set():
                callback_executed.set()

            callback(obsws, event)

    obsws.register_event_handler(type_name, wrapped_callback)

    try:
        await asyncio.wait_for(callback_executed.wait(), timeout, loop=loop)

    except asyncio.TimeoutError:
        raise EventNotReceived(
            "The event wasn't received in", timeout, "seconds")

    finally:
        obsws.unregister_event_handler(type_name, wrapped_callback)


# =============================================================================
# >> TESTS
# =============================================================================
class TestLogging(BaseOBSWSTest):
    @classmethod
    def setUpClass(cls):
        obwsrc_logger.setLevel(logging.ERROR)

    @async_test
    async def test_event_handler_exceptions(self):
        def broken_callback(obsws, event):
            raise ValueError("Intentional exception")

        with self.assertLogs(obwsrc_logger, 'ERROR') as log_hook:
            try:
                await wait_for_event(
                    self.obsws, REF_EVENT, broken_callback,
                    REF_EVENT_AWAITING_TIMEOUT, loop=self.loop)

            except EventNotReceived:
                self.skipTest(
                    "OBS Studio should be sending regular {type_name} events "
                    "to perform this test".format(type_name=REF_EVENT))

        for record in log_hook.records:
            record.level = logging.DEBUG
            root_logger.handle(record)

        await asyncio.sleep(1, loop=self.loop)

    @async_test
    async def test_async_event_handler_exceptions(self):
        async def broken_callback(obsws, event):
            await asyncio.sleep(1, loop=self.loop)
            raise ValueError("Intentional exception")

        with self.assertLogs(obwsrc_logger, 'ERROR') as log_hook:
            try:
                await wait_for_event(
                    self.obsws, REF_EVENT, broken_callback,
                    REF_EVENT_AWAITING_TIMEOUT, loop=self.loop)

                await asyncio.sleep(2, loop=self.loop)

            except EventNotReceived:
                self.skipTest(
                    "OBS Studio should be sending regular {type_name} events "
                    "to perform this test".format(type_name=REF_EVENT))

        for record in log_hook.records:
            record.level = logging.DEBUG
            root_logger.handle(record)

        await asyncio.sleep(1, loop=self.loop)


# =============================================================================
# >> RUN TESTS
# =============================================================================
if __name__ == '__main__':
    root_logger = logging.getLogger("Testing")
    root_logger.setLevel(logging.DEBUG)
    root_logger.addHandler(logging.StreamHandler(stream=sys.stdout))
    unittest.main(verbosity=2)
