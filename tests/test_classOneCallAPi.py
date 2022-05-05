"""Test Module: OneCallApiAlerts."""
import pytest

from pocar.OneCallApi import OneCallApi

# CONSTANT DATA
LAT = 45.1234
LON = 1.2345
KEY = "abcdef1234567890abcdef1234567890"
EXC = "current,minutely,daily,hourly,alerts"
URL = f"https://api.openweathermap.org/data/2.5/onecall?lat={LAT}&lon={LON}&exclude={EXC}&units=metric&appid={KEY}"

RAW_DATA = {
    "lat": 45.1234,
    "lon": 1.2345,
    "timezone": "Europe/Paris",
    "timezone_offset": 7200,
}


def test_0000():
    """Test: validate constructor nominal case."""
    oca = OneCallApi(LAT, LON, KEY, EXC)
    assert oca.lat == LAT
    assert oca.lon == LON
    assert oca.key == KEY
    assert oca.exc == EXC


def test_0001():
    """Test: validate constructor for latitude."""
    # case greater than
    with pytest.raises(ValueError):
        OneCallApi(91, LON, KEY, EXC)
    # case lesser than
    with pytest.raises(ValueError):
        OneCallApi(-91, LON, KEY, EXC)


def test_0002():
    """Test: validate constructor for longitude."""
    # case greater than
    with pytest.raises(ValueError):
        OneCallApi(LAT, 181, KEY, EXC)
    # case lesser than
    with pytest.raises(ValueError):
        OneCallApi(LAT, -181, KEY, EXC)


def test_0003():
    """Test: validate constructor for key."""
    # case short key
    with pytest.raises(ValueError):
        OneCallApi(LAT, LON, "abcdef1234567890abcdef12345678XX", EXC)
    # case non-hexadecimal key
    with pytest.raises(ValueError):
        OneCallApi(LAT, LON, "abcdef1234567890abcdef", EXC)


def test_0004():
    """Test: validate constructor for exc."""
    # case empty excluded string
    oca = OneCallApi(LAT, LON, KEY, "")
    assert oca.exc == ""
    # case invalid characters
    with pytest.raises(ValueError):
        for char in '@^! #%$&)(+*-="':
            OneCallApi(LAT, LON, KEY, char)
    # case invalid word
    with pytest.raises(ValueError):
        OneCallApi(LAT, LON, KEY, "toto,tata")


def test_0005():
    """Test: validate method config."""
    oca = OneCallApi(LAT, LON, KEY, EXC)
    conf_dict = oca.config()
    assert type(conf_dict) is dict
    assert conf_dict["lat"] == LAT
    assert conf_dict["lon"] == LON
    assert conf_dict["key"] == KEY
    assert conf_dict["exc"] == EXC
    assert conf_dict["url"] == URL


def test_0006():
    """Test: validate method raw_data."""
    oca = OneCallApi(LAT, LON, KEY, EXC)
    oca._rawdata = RAW_DATA
    data_dict = oca.raw_data()
    assert type(data_dict) is dict
    assert data_dict["lat"] == 45.1234
    assert data_dict["lon"] == 1.2345
    assert data_dict["timezone"] == "Europe/Paris"
    assert data_dict["timezone_offset"] == 7200


@pytest.mark.filterwarnings("ignore:Unverified HTTPS request is being made.*")
def test_0007():
    """Test: validate method update_data."""
    oca = OneCallApi(LAT, LON, KEY, EXC)
    assert oca.update_data() is False


def test_0008():
    """Test: validate method timezone."""
    oca = OneCallApi(LAT, LON, KEY, EXC)
    oca._rawdata = RAW_DATA
    assert oca.timezone() == RAW_DATA["timezone"]


def test_0009():
    """Test: validate method timezone_offset."""
    oca = OneCallApi(LAT, LON, KEY, EXC)
    oca._rawdata = RAW_DATA
    assert oca.timezone_offset() == RAW_DATA["timezone_offset"]


def test_0010():
    """Test: validate method timestamp."""
    value = 12345
    oca = OneCallApi(LAT, LON, KEY, EXC)
    oca._timestamp = value
    assert oca.timestamp() == value
