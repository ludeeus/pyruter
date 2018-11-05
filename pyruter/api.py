"""
A module to get information about the next departure from a stop.

This code is released under the terms of the MIT license. See the LICENSE
file for more details.
"""
from .common import BASE_URL, LOGGER
from .error import RuterError


class Departures():
    """A class to get departure information."""

    def __init__(self, loop, stopid, destination=None):
        """Initialize the class."""
        self.loop = loop
        self.stopid = stopid
        self.destination = destination
        self._departures = []

    async def get_departures(self):
        """Get departure info from stopid."""
        from .common import CommonFunctions
        common = CommonFunctions(self.loop)
        departures = []
        endpoint = '{}/StopVisit/GetDepartures/{}'.format(BASE_URL,
                                                          str(self.stopid))
        data = await common.api_call(endpoint)
        for entries in data:
            try:
                data = entries['MonitoredVehicleJourney']
                if self.destination is not None:
                    if data['DestinationName'] == self.destination:
                        data = entries['MonitoredVehicleJourney']
                        line = data['LineRef']
                        destinationname = data['DestinationName']
                        monitored = data['MonitoredCall']
                        time = monitored['ExpectedDepartureTime']
                        departures.append({"time": time,
                                           "line": line,
                                           "destination": destinationname})
                else:
                    data = entries['MonitoredVehicleJourney']
                    line = data['LineRef']
                    destinationname = data['DestinationName']
                    monitored = data['MonitoredCall']
                    time = monitored['ExpectedDepartureTime']
                    departures.append({"time": time,
                                       "line": line,
                                       "destination": destinationname})
            except RuterError as error:
                LOGGER.error('Error connecting to Ruter, %s', error)
        self._departures = await common.sort_data(departures, 'time')

    @property
    def departures(self):
        """Return the departures."""
        return self._departures
