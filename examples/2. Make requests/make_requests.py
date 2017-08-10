"""Example shows how to send requests and get responses."""

import asyncio

from obswsrc import OBSWS
from obswsrc.requests import ResponseStatus, StartStreamingRequest
from obswsrc.types import Stream, StreamSettings


async def main():

    async with OBSWS('localhost', 4444, "password") as obsws:

        # We can send an empty StartStreaming request (in that case the plugin
        # will use OBS configuration), but let's provide some settings as well
        stream_settings = StreamSettings(
            server="rtmp://example.org/my_application",
            key="secret_stream_key",
            use_auth=False
        )
        stream = Stream(
            settings=stream_settings,
            type="rtmp_custom",
        )

        # Now let's actually perform a request
        response = await obsws.require(StartStreamingRequest(stream=stream))

        # Check if everything is OK
        if response.status == ResponseStatus.OK:
            print("Streaming has started")
        else:
            print("Couldn't start the stream! Reason:", response.error)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
