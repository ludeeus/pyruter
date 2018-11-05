"""Common attributes and functions."""
import logging

import aiohttp
import async_timeout

from .error import RuterError

LOGGER = logging.getLogger(__name__)
BASE_URL = 'http://reisapi.ruter.no'


class CommonFunctions():
    """A class for common functions."""

    def __init__(self, loop):
        """Initialize the class."""
        self.loop = loop

    async def api_call(self, endpoint):
        """Api call."""
        data = None
        try:
            async with async_timeout.timeout(5, loop=self.loop):
                async with aiohttp.ClientSession() as session:
                    response = await session.get(endpoint)
                    data = await response.json()
        except RuterError as error:
            LOGGER.error('Error connecting to Ruter, %s', error)
        return data

    async def sort_data(self, data, sort_key, reverse=False):
        """Sort dataset."""
        sorted_data = []
        lines = sorted(data, key=lambda k: k[sort_key], reverse=reverse)
        for line in lines:
            sorted_data.append(line)
        return sorted_data
