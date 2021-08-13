import openweathermap

# CONSTANT DATA
LAT = 45.1234
LON = 1.2345
KEY = "abcdef1234567890abcdef1234567890"
EXC = "current,hourly,minutely,daily"
URL = f"https://api.openweathermap.org/data/2.5/onecall?lat={LAT}&lon={LON}" f"&exclude={EXC}&units=metric&appid={KEY}"

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


# Test: validate constructor nominal case
def test_0000():
    ocaa = openweathermap.OneCallApiAlerts(LAT, LON, KEY)
    assert ocaa.lat == LAT
    assert ocaa.lon == LON
    assert ocaa.key == KEY
    assert ocaa.exc == EXC


# Test: validate method raw_data_alerts
def test_0001():
    ocaa = openweathermap.OneCallApiAlerts(LAT, LON, KEY)
    ocaa._rawdata = RAW_DATA_ALERTS
    assert ocaa.raw_data_alerts() == RAW_DATA_ALERTS["alerts"]


# Test: validate method sender_name
def test_0002():
    ocaa = openweathermap.OneCallApiAlerts(LAT, LON, KEY)
    ocaa._rawdata = RAW_DATA_ALERTS
    assert ocaa.sender_name() == RAW_DATA_ALERTS["alerts"][0]["sender_name"]


# Test: validate method event
def test_0003():
    ocaa = openweathermap.OneCallApiAlerts(LAT, LON, KEY)
    ocaa._rawdata = RAW_DATA_ALERTS
    assert ocaa.event() == RAW_DATA_ALERTS["alerts"][0]["event"]


# Test: validate method start_dt
def test_0004():
    ocaa = openweathermap.OneCallApiAlerts(LAT, LON, KEY)
    ocaa._rawdata = RAW_DATA_ALERTS
    assert ocaa.start_dt(1) == RAW_DATA_ALERTS["alerts"][0]["start"]


# Test: validate method end_dt
def test_0005():
    ocaa = openweathermap.OneCallApiAlerts(LAT, LON, KEY)
    ocaa._rawdata = RAW_DATA_ALERTS
    assert ocaa.end_dt(1) == RAW_DATA_ALERTS["alerts"][0]["end"]


# Test: validate method description
def test_0006():
    ocaa = openweathermap.OneCallApiAlerts(LAT, LON, KEY)
    ocaa._rawdata = RAW_DATA_ALERTS
    assert ocaa.description() == RAW_DATA_ALERTS["alerts"][0]["description"]


# Test: validate method tags
def test_0007():
    ocaa = openweathermap.OneCallApiAlerts(LAT, LON, KEY)
    ocaa._rawdata = RAW_DATA_ALERTS
    assert ocaa.tags() == RAW_DATA_ALERTS["alerts"][0]["tags"]
