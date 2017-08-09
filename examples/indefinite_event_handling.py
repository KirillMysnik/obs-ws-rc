import asyncio
import logging
import sys

from obswsrc import OBSWS
from obswsrc.events import events
from obswsrc.logs import logger


# We will output logging to sys.stdout, as many events might raise errors
# on creation (that's because protocol.json is not perfect) - such errors
# are logged by obs-ws-rc automatically, we just need to see them
logger.setLevel(logging.ERROR)
logger.addHandler(logging.StreamHandler(stream=sys.stdout))


def event_handler(obsws, event):
    # This is a regular handler, it can't require information from
    # OBSWS instances

    print("Regular Handler received '{}' event!".format(event.update_type))


async def async_event_handler(obsws, event):
    # Now this is an async handler which can safely await for things, e.g.
    # it can do "await obsws.require(...)" here

    print("Async Handler received '{}' event!".format(event.update_type))

    # Even when your async event handler awaits for something, it doesn't
    # prevent handling of further events
    await asyncio.sleep(10)


async def main():

    # Note that the loop can only be passed as a keyword argument
    async with OBSWS('localhost', 4444, "password") as obsws:

        print("Connection established.")

        # Let's walk through all known events...
        for name in events.keys():

            # And attach two handlers (regular and async) to each of them
            obsws.register_event_handler(name, event_handler)
            obsws.register_event_handler(name, async_event_handler)

        # We don't want to exit the OBSWS context right there, so we await
        # til the sock gets closed - meanwhile all events will be processed
        await obsws

        print("Connection terminated.")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
