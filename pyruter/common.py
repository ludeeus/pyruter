"""Common attributes and functions."""
import logging
import asyncio
import aiohttp
import async_timeout

LOGGER = logging.getLogger(__name__)
BASE_URL = 'http://reisapi.ruter.no'
HEADERS = {'Content-Type': 'application/json', 'Accept': 'application/json'}


class CommonFunctions():
    """A class for common functions."""

    def __init__(self, loop, session):
        """Initialize the class."""
        self.loop = loop
        self.session = session

    async def api_call(self, endpoint):
        """Call the API."""
        data = None
        if self.session is None:
            self.session = aiohttp.ClientSession()
        try:
            async with async_timeout.timeout(5, loop=self.loop):
                response = await self.session.get(endpoint, headers=HEADERS)
                data = await response.json()
        except aiohttp.ClientError as error:
            LOGGER.error('Error connecting to Ruter, %s', error)
        except asyncio.TimeoutError as error:
            LOGGER.debug('Timeout connecting to Ruter, %s', error)
        return data

    async def sort_data(self, data, sort_key, reverse=False):
        """Sort dataset."""
        sorted_data = []
        lines = sorted(data, key=lambda k: k[sort_key], reverse=reverse)
        for line in lines:
            sorted_data.append(line)
        return sorted_data
