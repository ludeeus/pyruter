"""CLI commands."""
import asyncio
import json
import click
import aiohttp


@click.group()
def commands():
    """Click group."""
    pass


@commands.command()
@click.option('--stop', '-S', type=int, default=None,
              help="Stop ID of the stop you want information from.")
@click.option('--destination', '-D', type=str, default=None,
              help="Name of final destination.")
def departure(stop, destination):
    """Get departure information."""
    from pyruter.api import Departures

    async def get_departures():
        """Get departure information."""
        async with aiohttp.ClientSession() as session:
            data = Departures(LOOP, stop, destination, session)
            await data.get_departures()
            print(json.dumps(data.departures, indent=4, sort_keys=True))
    LOOP.run_until_complete(get_departures())


LOOP = asyncio.get_event_loop()
CLI = click.CommandCollection(sources=[commands])
