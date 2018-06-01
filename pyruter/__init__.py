
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
        self.stopInfo = None

    def getDepartureInfo(self, stopid, destinationName = None):
        """Get departure info from stopid."""
        fetchurl = self.BASE_URL + str(stopid)
        try:
            departureRequest = requests.get(fetchurl, timeout=2).json()
        except:
            stopInfo = None
        else:
            if not destinationName:
                departureResponse = departureRequest[0]['MonitoredVehicleJourney']
            else:
                count = 0
                stop = 0
                while stop != 1:
                    departureResponse = departureRequest[count]['MonitoredVehicleJourney']
                    if departureResponse['DestinationName'] == destinationName:
                        departureResponse = departureRequest[count]['MonitoredVehicleJourney']
                        stop = 1
                    else:
                        count = count + 1
            line = departureResponse['LineRef']
            destination = departureResponse['DestinationName']
            time = departureResponse['MonitoredCall']['ExpectedDepartureTime']
            stopInfo = [time, line, destination]
        return stopInfo
