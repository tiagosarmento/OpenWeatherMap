import openweathermap
import pytest

# CONSTANT DATA
LAT = 43.58
LON = 7.19
KEY = "abcdef1234567890abcdef1234567890"
EXC = "current,daily,hourly,alerts"
URL = (
    f"https://api.openweathermap.org/data/2.5/onecall?lat={LAT}&lon={LON}"
    f"&exclude={EXC}&units=metric&appid={KEY}"
)


# Test: validate constructor nominal case
def test_0000():
    # case nominal
    oca = openweathermap.OneCallApi(LAT, LON, KEY, EXC)
    assert oca.lat == LAT
    assert oca.lon == LON
    assert oca.key == KEY


# Test: validate constructor for latitude
def test_0001():
    # case greater than
    with pytest.raises(ValueError):
        openweathermap.OneCallApi(91, LON, KEY, EXC)
    # case lesser than
    with pytest.raises(ValueError):
        openweathermap.OneCallApi(-91, LON, KEY, EXC)


# Test: validate constructor for longitude
def test_0002():
    # case greater than
    with pytest.raises(ValueError):
        openweathermap.OneCallApi(LAT, 181, KEY, EXC)
    # case lesser than
    with pytest.raises(ValueError):
        openweathermap.OneCallApi(LAT, -181, KEY, EXC)


# Test: validate constructor for key
def test_0003():
    # case short key
    with pytest.raises(ValueError):
        openweathermap.OneCallApi(LAT, LON, "abcdef1234567890abcdef12345678XX", EXC)
    # case non-hexadecimal key
    with pytest.raises(ValueError):
        openweathermap.OneCallApi(LAT, LON, "abcdef1234567890abcdef", EXC)


# Test: validate method config
def test_0004():
    oca = openweathermap.OneCallApi(LAT, LON, KEY, EXC)
    conf_dict = oca.config()
    assert type(conf_dict) is dict
    assert conf_dict["lat"] == LAT
    assert conf_dict["lon"] == LON
    assert conf_dict["key"] == KEY
    assert conf_dict["exc"] == EXC
    assert conf_dict["url"] == URL


# Test: validate method raw_data
def test_0005():
    oca = openweathermap.OneCallApi(LAT, LON, KEY, EXC)
    data_dict = oca.raw_data()
    assert type(data_dict) is dict


# Test: validate method updateData
@pytest.mark.filterwarnings("ignore:Unverified HTTPS request is being made.*")
def test_0006():
    oca = openweathermap.OneCallApi(LAT, LON, KEY, EXC)
    assert oca.updateData() is False


# Test: validate method timezone
def test_0007():
    oca = openweathermap.OneCallApi(LAT, LON, KEY, EXC)
    assert oca.timezone() == ""


# Test: validate method timezone_offset
def test_0008():
    oca = openweathermap.OneCallApi(LAT, LON, KEY, EXC)
    assert oca.timezone_offset() == ""


# Test: validate method timestamp
def test_0009():
    oca = openweathermap.OneCallApi(LAT, LON, KEY, EXC)
    assert oca.timestamp() == 0
