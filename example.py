"""Example usage of pyruter."""
import asyncio
from pyruter.api import Departures

async def test():
    """Example usage of pyruter."""
    stopid = 2190400
    destination = 'Drammen'
    data = Departures(LOOP, stopid, destination)
    await data.get_departures()

    print("Departures:", data.departures)

LOOP = asyncio.get_event_loop()
LOOP.run_until_complete(test())
