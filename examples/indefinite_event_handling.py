import asyncio

from obswsrc import OBSWS
from obswsrc.events import events


def event_handler(obsws, event):
    # This is a regular handler, it can't require information from
    # OBSWS instances

    print("Regular Handler received '{}' event!".format(event.update_type))


async def async_event_handler(obsws, event):
    # Now this is an async handler which can safely await for things, e.g.
    # it can do "await obsws.require(...)" here

    print("Async Handler received '{}' event!".format(event.update_type))

    # Even when your async event handler awaits for something, it doesn't
    # prevent handling of further events.
    await asyncio.sleep(10)


async def main(loop):

    # Note that the loop can only be passed as a keyword argument
    async with OBSWS('localhost', 4444, "password", loop=loop) as obsws:

        # Let's walk through all known events...
        for name in events.keys():

            # And attach two handlers (regular and async) to each of them
            obsws.register_event_handler(name, event_handler)
            obsws.register_event_handler(name, async_event_handler)

        # We don't want to exit the OBSWS context right there, so we await
        # til the sock gets closed - meanwhile all events will be processed
        await obsws.sock_closed()


loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()
