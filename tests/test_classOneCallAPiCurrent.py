"""Test Module: OneCallApiCurrent."""
from pocar.OneCallApiCurrent import OneCallApiCurrent

# CONSTANT DATA
LAT = 45.1234
LON = 1.2345
KEY = "abcdef1234567890abcdef1234567890"
EXC = "minutely,daily,hourly,alerts"
URL = f"https://api.openweathermap.org/data/2.5/onecall?lat={LAT}&lon={LON}&exclude={EXC}&units=metric&appid={KEY}"

RAW_DATA_CURRENT = {
    "lat": 45.1234,
    "lon": 1.2345,
    "timezone": "Europe/Paris",
    "timezone_offset": 7200,
    "current": {
        "dt": 1628526292,
        "sunrise": 1628483379,
        "sunset": 1628534674,
        "temp": 27.19,
        "feels_like": 28.74,
        "pressure": 1017,
        "humidity": 65,
        "dew_point": 20.04,
        "uvi": 1.68,
        "clouds": 0,
        "visibility": 10000,
        "wind_speed": 2.57,
        "wind_deg": 110,
        "weather": [{"id": 800, "main": "Clear", "description": "clear sky", "icon": "01d"}],
    },
}


def test_0000():
    """Test: validate constructor nominal case."""
    ocac = OneCallApiCurrent(LAT, LON, KEY)
    assert ocac.lat == LAT
    assert ocac.lon == LON
    assert ocac.key == KEY
    assert ocac.exc == EXC


def test_0001():
    """Test: validate method data time."""
    ocac = OneCallApiCurrent(LAT, LON, KEY)
    ocac._rawdata = RAW_DATA_CURRENT
    assert ocac.data_time(1) == RAW_DATA_CURRENT["current"]["dt"]


def test_0002():
    """Test: validate method Sunrise time."""
    ocac = OneCallApiCurrent(LAT, LON, KEY)
    ocac._rawdata = RAW_DATA_CURRENT
    assert ocac.sunrise(1) == RAW_DATA_CURRENT["current"]["sunrise"]


def test_0003():
    """Test: validate method Sunset time."""
    ocac = OneCallApiCurrent(LAT, LON, KEY)
    ocac._rawdata = RAW_DATA_CURRENT
    assert ocac.sunset(1) == RAW_DATA_CURRENT["current"]["sunset"]


def test_0004():
    """Test: validate method temperature."""
    ocac = OneCallApiCurrent(LAT, LON, KEY)
    ocac._rawdata = RAW_DATA_CURRENT
    assert ocac.temperature() == RAW_DATA_CURRENT["current"]["temp"]


def test_0005():
    """Test: validate method temperature_feels_like."""
    ocac = OneCallApiCurrent(LAT, LON, KEY)
    ocac._rawdata = RAW_DATA_CURRENT
    assert ocac.temperature_feels_like() == RAW_DATA_CURRENT["current"]["feels_like"]


def test_0006():
    """Test: validate method pressure."""
    ocac = OneCallApiCurrent(LAT, LON, KEY)
    ocac._rawdata = RAW_DATA_CURRENT
    assert ocac.pressure() == RAW_DATA_CURRENT["current"]["pressure"]


def test_0007():
    """Test: validate method humidity."""
    ocac = OneCallApiCurrent(LAT, LON, KEY)
    ocac._rawdata = RAW_DATA_CURRENT
    assert ocac.humidity() == RAW_DATA_CURRENT["current"]["humidity"]


def test_0008():
    """Test: validate method dew_point."""
    ocac = OneCallApiCurrent(LAT, LON, KEY)
    ocac._rawdata = RAW_DATA_CURRENT
    assert ocac.dew_point() == RAW_DATA_CURRENT["current"]["dew_point"]


def test_0009():
    """Test: validate method clouds."""
    ocac = OneCallApiCurrent(LAT, LON, KEY)
    ocac._rawdata = RAW_DATA_CURRENT
    assert ocac.clouds() == RAW_DATA_CURRENT["current"]["clouds"]


def test_0010():
    """Test: validate method uvi."""
    ocac = OneCallApiCurrent(LAT, LON, KEY)
    ocac._rawdata = RAW_DATA_CURRENT
    assert ocac.uvi() == RAW_DATA_CURRENT["current"]["uvi"]


def test_0011():
    """Test: validate method visibility."""
    ocac = OneCallApiCurrent(LAT, LON, KEY)
    ocac._rawdata = RAW_DATA_CURRENT
    assert ocac.visibility() == RAW_DATA_CURRENT["current"]["visibility"]


def test_0012():
    """Test: validate method wind_speed."""
    ocac = OneCallApiCurrent(LAT, LON, KEY)
    ocac._rawdata = RAW_DATA_CURRENT
    assert ocac.wind_speed() == RAW_DATA_CURRENT["current"]["wind_speed"]


def test_0013():
    """Test: validate method wind_gust."""
    ocac = OneCallApiCurrent(LAT, LON, KEY)
    ocac._rawdata = RAW_DATA_CURRENT
    assert ocac.wind_gust() == "N/A"


def test_0014():
    """Test: validate method wind_deg."""
    ocac = OneCallApiCurrent(LAT, LON, KEY)
    ocac._rawdata = RAW_DATA_CURRENT
    assert ocac.wind_deg() == RAW_DATA_CURRENT["current"]["wind_deg"]


def test_0015():
    """Test: validate method rain_volume."""
    ocac = OneCallApiCurrent(LAT, LON, KEY)
    ocac._rawdata = RAW_DATA_CURRENT
    assert ocac.rain_volume() == "N/A"


def test_0016():
    """Test: validate method snow_volume."""
    ocac = OneCallApiCurrent(LAT, LON, KEY)
    ocac._rawdata = RAW_DATA_CURRENT
    assert ocac.snow_volume() == "N/A"


def test_0017():
    """Test: validate method weather_condition_id."""
    ocac = OneCallApiCurrent(LAT, LON, KEY)
    ocac._rawdata = RAW_DATA_CURRENT
    assert ocac.weather_condition_id() == RAW_DATA_CURRENT["current"]["weather"][0]["id"]


def test_0018():
    """Test: validate method weather_condition_main."""
    ocac = OneCallApiCurrent(LAT, LON, KEY)
    ocac._rawdata = RAW_DATA_CURRENT
    assert ocac.weather_condition_main() == RAW_DATA_CURRENT["current"]["weather"][0]["main"]


def test_0019():
    """Test: validate method weather_condition_description."""
    ocac = OneCallApiCurrent(LAT, LON, KEY)
    ocac._rawdata = RAW_DATA_CURRENT
    assert ocac.weather_condition_description() == RAW_DATA_CURRENT["current"]["weather"][0]["description"]


def test_0020():
    """Test: validate method weather_condition_icon."""
    ocac = OneCallApiCurrent(LAT, LON, KEY)
    ocac._rawdata = RAW_DATA_CURRENT
    assert ocac.weather_condition_icon() == RAW_DATA_CURRENT["current"]["weather"][0]["icon"]


def test_0021():
    """Test: validate method raw data current."""
    ocac = OneCallApiCurrent(LAT, LON, KEY)
    ocac._rawdata = RAW_DATA_CURRENT
    assert ocac.raw_data_current() == RAW_DATA_CURRENT["current"]
