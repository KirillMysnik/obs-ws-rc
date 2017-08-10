"""Example shows how to use :mod:`asyncio` module API to avoid blocking forever
while awaiting for an event."""

import asyncio

from obswsrc import OBSWS
from obswsrc.requests import StartStopStreamingRequest


async def main():

    async with OBSWS('localhost', 4444, "password") as obsws:

        print("Connection established.")

        # We will be sending StartStopStreaming requests if no events are
        # received in 10 seconds

        while True:
            try:

                # Await for an event, but at most for 10 seconds
                event = await asyncio.wait_for(obsws.event(), 10)

            except asyncio.TimeoutError:

                # Event wasn't acquired, it's just timeout
                # Time to toggle streaming
                await obsws.require(StartStopStreamingRequest())
                print("Toggled streaming")

            else:
                if event is None:
                    break

                print("Awaited for '{}' event!".format(event.type_name))

        print("Connection terminated.")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
