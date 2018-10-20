"""
A module to get information about the next departure from a stop.

This code is released under the terms of the MIT license. See the LICENSE
file for more details.
"""
import requests


class Ruter:
    """This class is used to get departure information from Ruter."""

    BASE_URL = 'http://reisapi.ruter.no/StopVisit/GetDepartures/'

    def __init__(self):
        """Initialize."""

    def get_departure_info(self, stopid, destination=None):
        """Get departure info from stopid."""
        stop_info = []
        fetchurl = self.BASE_URL + str(stopid)
        try:
            response = requests.get(fetchurl, timeout=8).json()
        except ConnectionError:
            stop_info.append({"success": False})
        else:
            stop_info.append({"success": True})
            for entries in response:
                try:
                    data = entries['MonitoredVehicleJourney']
                    if destination is not None:
                        if data['DestinationName'] == destination:
                            data = entries['MonitoredVehicleJourney']
                            line = data['LineRef']
                            destinationname = data['DestinationName']
                            monitored = data['MonitoredCall']
                            time = monitored['ExpectedDepartureTime']
                    else:
                        data = entries['MonitoredVehicleJourney']
                        line = data['LineRef']
                        destinationname = data['DestinationName']
                        monitored = data['MonitoredCall']
                        time = monitored['ExpectedDepartureTime']
                    stop_info.append({"time": time,
                                      "line": line,
                                      "destination": destinationname})
                except IndexError:
                    stop_info.append({"success": False})
        return stop_info


def self_test():
    """Run a test of the functions in this module."""
    stopid = 2190255
    destination = 'Oslo bussterminal'
    print(Ruter().get_departure_info(stopid))
    print(Ruter().get_departure_info(stopid, destination))
