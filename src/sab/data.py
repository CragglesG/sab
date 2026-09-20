import xml.etree.ElementTree as ET

import requests


class Station:
    def __init__(self, name, alias, lat, long, code, id):
        self.name = name.text
        self.alias = alias.text if alias != "None" else None
        self.lat = lat.text
        self.long = long.text
        self.code = code.text
        self.id = id.text

class RailAPI:
    def __init__(self):
        pass

    def get_stations(self, station_type = "A"):
        """Get a list of stations in Ireland. station_type can be A for All, M for Mainline, S for Suburban and D for DART"""
        stations_data = requests.get(f"https://api.irishrail.ie/realtime/realtime.asmx/getAllStationsXML_WithStationType?StationType={station_type}")

        stations = [Station(*station) for station in ET.fromstring(stations_data.content)]

        return stations
