import pytest
from sab.data import RailAPI, Station

def test_get_stations():
    api = RailAPI()

    stations = api.get_stations("A")

    assert isinstance(stations, list)

    assert isinstance(stations[0].__dict__, dict)

    assert isinstance(stations[0], Station)

    assert stations[0].name == "Belfast"
