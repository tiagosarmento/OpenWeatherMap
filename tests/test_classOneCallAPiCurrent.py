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


# Test: validate constructor nominal case
def test_0000():
    ocac = OneCallApiCurrent(LAT, LON, KEY)
    assert ocac.lat == LAT
    assert ocac.lon == LON
    assert ocac.key == KEY
    assert ocac.exc == EXC


# Test: validate method data time
def test_0001():
    ocac = OneCallApiCurrent(LAT, LON, KEY)
    ocac._rawdata = RAW_DATA_CURRENT
    assert ocac.data_time(1) == RAW_DATA_CURRENT["current"]["dt"]


# Test: validate method Sunrise time
def test_0002():
    ocac = OneCallApiCurrent(LAT, LON, KEY)
    ocac._rawdata = RAW_DATA_CURRENT
    assert ocac.sunrise(1) == RAW_DATA_CURRENT["current"]["sunrise"]


# Test: validate method Sunset time
def test_0003():
    ocac = OneCallApiCurrent(LAT, LON, KEY)
    ocac._rawdata = RAW_DATA_CURRENT
    assert ocac.sunset(1) == RAW_DATA_CURRENT["current"]["sunset"]


# Test: validate method temperature
def test_0004():
    ocac = OneCallApiCurrent(LAT, LON, KEY)
    ocac._rawdata = RAW_DATA_CURRENT
    assert ocac.temperature() == RAW_DATA_CURRENT["current"]["temp"]


# Test: validate method temperature_feels_like
def test_0005():
    ocac = OneCallApiCurrent(LAT, LON, KEY)
    ocac._rawdata = RAW_DATA_CURRENT
    assert ocac.temperature_feels_like() == RAW_DATA_CURRENT["current"]["feels_like"]


# Test: validate method pressure
def test_0006():
    ocac = OneCallApiCurrent(LAT, LON, KEY)
    ocac._rawdata = RAW_DATA_CURRENT
    assert ocac.pressure() == RAW_DATA_CURRENT["current"]["pressure"]


# Test: validate method humidity
def test_0007():
    ocac = OneCallApiCurrent(LAT, LON, KEY)
    ocac._rawdata = RAW_DATA_CURRENT
    assert ocac.humidity() == RAW_DATA_CURRENT["current"]["humidity"]


# Test: validate method dew_point
def test_0008():
    ocac = OneCallApiCurrent(LAT, LON, KEY)
    ocac._rawdata = RAW_DATA_CURRENT
    assert ocac.dew_point() == RAW_DATA_CURRENT["current"]["dew_point"]


# Test: validate method clouds
def test_0009():
    ocac = OneCallApiCurrent(LAT, LON, KEY)
    ocac._rawdata = RAW_DATA_CURRENT
    assert ocac.clouds() == RAW_DATA_CURRENT["current"]["clouds"]


# Test: validate method uvi
def test_0010():
    ocac = OneCallApiCurrent(LAT, LON, KEY)
    ocac._rawdata = RAW_DATA_CURRENT
    assert ocac.uvi() == RAW_DATA_CURRENT["current"]["uvi"]


# Test: validate method visibility
def test_0011():
    ocac = OneCallApiCurrent(LAT, LON, KEY)
    ocac._rawdata = RAW_DATA_CURRENT
    assert ocac.visibility() == RAW_DATA_CURRENT["current"]["visibility"]


# Test: validate method wind_speed
def test_0012():
    ocac = OneCallApiCurrent(LAT, LON, KEY)
    ocac._rawdata = RAW_DATA_CURRENT
    assert ocac.wind_speed() == RAW_DATA_CURRENT["current"]["wind_speed"]


# Test: validate method wind_gust
def test_0013():
    ocac = OneCallApiCurrent(LAT, LON, KEY)
    ocac._rawdata = RAW_DATA_CURRENT
    assert ocac.wind_gust() == "N/A"


# Test: validate method wind_deg
def test_0014():
    ocac = OneCallApiCurrent(LAT, LON, KEY)
    ocac._rawdata = RAW_DATA_CURRENT
    assert ocac.wind_deg() == RAW_DATA_CURRENT["current"]["wind_deg"]


# Test: validate method rain_volume
def test_0015():
    ocac = OneCallApiCurrent(LAT, LON, KEY)
    ocac._rawdata = RAW_DATA_CURRENT
    assert ocac.rain_volume() == "N/A"


# Test: validate method snow_volume
def test_0016():
    ocac = OneCallApiCurrent(LAT, LON, KEY)
    ocac._rawdata = RAW_DATA_CURRENT
    assert ocac.snow_volume() == "N/A"


# Test: validate method weather_condition_id
def test_0017():
    ocac = OneCallApiCurrent(LAT, LON, KEY)
    ocac._rawdata = RAW_DATA_CURRENT
    assert ocac.weather_condition_id() == RAW_DATA_CURRENT["current"]["weather"][0]["id"]


# Test: validate method weather_condition_main
def test_0018():
    ocac = OneCallApiCurrent(LAT, LON, KEY)
    ocac._rawdata = RAW_DATA_CURRENT
    assert ocac.weather_condition_main() == RAW_DATA_CURRENT["current"]["weather"][0]["main"]


# Test: validate method weather_condition_description
def test_0019():
    ocac = OneCallApiCurrent(LAT, LON, KEY)
    ocac._rawdata = RAW_DATA_CURRENT
    assert ocac.weather_condition_description() == RAW_DATA_CURRENT["current"]["weather"][0]["description"]


# Test: validate method weather_condition_icon
def test_0020():
    ocac = OneCallApiCurrent(LAT, LON, KEY)
    ocac._rawdata = RAW_DATA_CURRENT
    assert ocac.weather_condition_icon() == RAW_DATA_CURRENT["current"]["weather"][0]["icon"]


# Test: validate method raw data current
def test_0021():
    ocac = OneCallApiCurrent(LAT, LON, KEY)
    ocac._rawdata = RAW_DATA_CURRENT
    assert ocac.raw_data_current() == RAW_DATA_CURRENT["current"]
