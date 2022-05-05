"""Test Module: OneCallApiAlerts."""
from pocar.OneCallApiAlerts import OneCallApiAlerts

# CONSTANT DATA
LAT = 45.1234
LON = 1.2345
KEY = "abcdef1234567890abcdef1234567890"
EXC = "current,hourly,minutely,daily"
URL = f"https://api.openweathermap.org/data/2.5/onecall?lat={LAT}&lon={LON}&exclude={EXC}&units=metric&appid={KEY}"

RAW_DATA_ALERTS = {
    "lat": 43.5832,
    "lon": 7.108,
    "timezone": "Europe/Paris",
    "timezone_offset": 7200,
    "alerts": [
        {
            "sender_name": "YYYY-XXXX",
            "event": "Severe high-temperature warning",
            "start": 1628863200,
            "end": 1628949600,
            "description": "THIS IS THE ALERT MESSAGE",
            "tags": ["Extreme temperature value"],
        }
    ],
}


def test_0000():
    """Test: validate constructor nominal case."""
    ocaa = OneCallApiAlerts(LAT, LON, KEY)
    assert ocaa.lat == LAT
    assert ocaa.lon == LON
    assert ocaa.key == KEY
    assert ocaa.exc == EXC


def test_0001():
    """Test: validate method raw_data_alerts."""
    ocaa = OneCallApiAlerts(LAT, LON, KEY)
    ocaa._rawdata = RAW_DATA_ALERTS
    assert ocaa.raw_data_alerts() == RAW_DATA_ALERTS["alerts"]


def test_0002():
    """Test: validate method sender_name."""
    ocaa = OneCallApiAlerts(LAT, LON, KEY)
    ocaa._rawdata = RAW_DATA_ALERTS
    assert ocaa.sender_name() == RAW_DATA_ALERTS["alerts"][0]["sender_name"]


def test_0003():
    """Test: validate method event."""
    ocaa = OneCallApiAlerts(LAT, LON, KEY)
    ocaa._rawdata = RAW_DATA_ALERTS
    assert ocaa.event() == RAW_DATA_ALERTS["alerts"][0]["event"]


def test_0004():
    """Test: validate method start_dt."""
    ocaa = OneCallApiAlerts(LAT, LON, KEY)
    ocaa._rawdata = RAW_DATA_ALERTS
    assert ocaa.start_dt(1) == RAW_DATA_ALERTS["alerts"][0]["start"]


def test_0005():
    """Test: validate method end_dt."""
    ocaa = OneCallApiAlerts(LAT, LON, KEY)
    ocaa._rawdata = RAW_DATA_ALERTS
    assert ocaa.end_dt(1) == RAW_DATA_ALERTS["alerts"][0]["end"]


def test_0006():
    """Test: validate method description."""
    ocaa = OneCallApiAlerts(LAT, LON, KEY)
    ocaa._rawdata = RAW_DATA_ALERTS
    assert ocaa.description() == RAW_DATA_ALERTS["alerts"][0]["description"]


def test_0007():
    """Test: validate method tags."""
    ocaa = OneCallApiAlerts(LAT, LON, KEY)
    ocaa._rawdata = RAW_DATA_ALERTS
    assert ocaa.tags() == RAW_DATA_ALERTS["alerts"][0]["tags"]
