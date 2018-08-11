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
        """Initialize"""
        self.stop_info = None

    def get_departure_info(self, stopid, destination=None):
        """Get departure info from stopid."""
        fetchurl = self.BASE_URL + str(stopid)
        try:
            departure_request = requests.get(fetchurl, timeout=2).json()
        except:
            stop_info = None
        else:
            if not destination:
                departure_response = departure_request[0]['MonitoredVehicleJourney']
            else:
                count = 0
                stop = 0
                while stop != 1:
                    departure_response = departure_request[count]['MonitoredVehicleJourney']
                    if departure_response['DestinationName'] == destination:
                        departure_response = departure_request[count]['MonitoredVehicleJourney']
                        stop = 1
                    else:
                        count = count + 1
            line = departure_response['LineRef']
            destination = departure_response['DestinationName']
            time = departure_response['MonitoredCall']['ExpectedDepartureTime']
            stop_info = [time, line, destination]
        return stop_info
