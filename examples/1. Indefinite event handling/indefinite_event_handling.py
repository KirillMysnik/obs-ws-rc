"""Example shows how to listen to events."""

import asyncio
import logging
import sys

from obswsrc import OBSWS
from obswsrc.logs import logger


# We will output logging to sys.stdout, as many events might raise errors
# on creation (that's because protocol.json is not perfect) - such errors
# are logged by obs-ws-rc automatically, we just need to see them
logger.setLevel(logging.ERROR)
logger.addHandler(logging.StreamHandler(stream=sys.stdout))


async def main():

    async with OBSWS('localhost', 4444, "password") as obsws:

        print("Connection established.")

        # We will receive events here by awaiting for them (you can await for
        # an event of a specific type by providing `type_name` argument to
        # the obsws.event() method)
        event = await obsws.event()

        # Awaited event might be None if connection is closed
        while event is not None:
            print("Awaited for '{}' event!".format(event.type_name))
            event = await obsws.event()

        print("Connection terminated.")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
