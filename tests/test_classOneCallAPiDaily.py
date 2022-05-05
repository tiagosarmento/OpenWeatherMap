"""Test Module: OneCallApiDaily."""
import pytest

from pocar.OneCallApiDaily import OneCallApiDaily

# CONSTANT DATA
LAT = 45.1234
LON = 1.2345
KEY = "abcdef1234567890abcdef1234567890"
EXC = "current,hourly,minutely,alerts"
URL = f"https://api.openweathermap.org/data/2.5/onecall?lat={LAT}&lon={LON}&exclude={EXC}&units=metric&appid={KEY}"

RAW_DATA_DAILY = {
    "lat": 43.5832,
    "lon": 7.108,
    "timezone": "Europe/Paris",
    "timezone_offset": 7200,
    "daily": [
        {
            "dt": 1628852400,
            "sunrise": 1628829249,
            "sunset": 1628879933,
            "moonrise": 1628848200,
            "moonset": 1628889660,
            "moon_phase": 0.17,
            "temp": {"day": 30.1, "min": 25.65, "max": 30.38, "night": 27.33, "eve": 29.35, "morn": 26.64},
            "feels_like": {"day": 31.53, "night": 28.03, "eve": 29.99, "morn": 26.64},
            "pressure": 1020,
            "humidity": 52,
            "dew_point": 19.17,
            "wind_speed": 2.79,
            "wind_deg": 106,
            "wind_gust": 3.04,
            "weather": [{"id": 800, "main": "Clear", "description": "clear sky", "icon": "01d"}],
            "clouds": 5,
            "pop": 0.01,
            "uvi": 8.48,
        },
        {
            "dt": 1628938800,
            "sunrise": 1628915717,
            "sunset": 1628966245,
            "moonrise": 1628938980,
            "moonset": 1628977620,
            "moon_phase": 0.21,
            "temp": {"day": 29.27, "min": 26.11, "max": 29.46, "night": 26.17, "eve": 28.94, "morn": 26.21},
            "feels_like": {"day": 30.42, "night": 26.17, "eve": 29.95, "morn": 26.21},
            "pressure": 1019,
            "humidity": 53,
            "dew_point": 17.43,
            "wind_speed": 2.79,
            "wind_deg": 122,
            "wind_gust": 3.27,
            "weather": [{"id": 800, "main": "Clear", "description": "clear sky", "icon": "01d"}],
            "clouds": 0,
            "pop": 0,
            "uvi": 8.55,
        },
        {
            "dt": 1629025200,
            "sunrise": 1629002184,
            "sunset": 1629052555,
            "moonrise": 1629029940,
            "moonset": 0,
            "moon_phase": 0.25,
            "temp": {"day": 28.63, "min": 25.59, "max": 28.74, "night": 25.59, "eve": 27.52, "morn": 25.64},
            "feels_like": {"day": 30.56, "night": 26.14, "eve": 29.25, "morn": 25.75},
            "pressure": 1016,
            "humidity": 61,
            "dew_point": 18.79,
            "wind_speed": 2.8,
            "wind_deg": 109,
            "wind_gust": 3.47,
            "weather": [{"id": 800, "main": "Clear", "description": "clear sky", "icon": "01d"}],
            "clouds": 0,
            "pop": 0,
            "uvi": 8.73,
        },
        {
            "dt": 1629111600,
            "sunrise": 1629088652,
            "sunset": 1629138865,
            "moonrise": 1629120960,
            "moonset": 1629065880,
            "moon_phase": 0.28,
            "temp": {"day": 26.89, "min": 24.31, "max": 26.89, "night": 24.33, "eve": 25.38, "morn": 24.31},
            "feels_like": {"day": 28.91, "night": 25.04, "eve": 26.11, "morn": 24.91},
            "pressure": 1012,
            "humidity": 73,
            "dew_point": 20.71,
            "wind_speed": 4.05,
            "wind_deg": 100,
            "wind_gust": 5.13,
            "weather": [{"id": 800, "main": "Clear", "description": "clear sky", "icon": "01d"}],
            "clouds": 9,
            "pop": 0.12,
            "uvi": 8.42,
        },
        {
            "dt": 1629198000,
            "sunrise": 1629175120,
            "sunset": 1629225173,
            "moonrise": 1629211800,
            "moonset": 1629154560,
            "moon_phase": 0.32,
            "temp": {"day": 26.12, "min": 23.52, "max": 26.26, "night": 24.43, "eve": 25.42, "morn": 23.97},
            "feels_like": {"day": 26.12, "night": 24.81, "eve": 25.85, "morn": 24.2},
            "pressure": 1013,
            "humidity": 66,
            "dew_point": 18.69,
            "wind_speed": 2.43,
            "wind_deg": 192,
            "wind_gust": 2.39,
            "weather": [{"id": 500, "main": "Rain", "description": "light rain", "icon": "10d"}],
            "clouds": 6,
            "pop": 0.36,
            "rain": 0.19,
            "uvi": 8.04,
        },
        {
            "dt": 1629284400,
            "sunrise": 1629261588,
            "sunset": 1629311480,
            "moonrise": 1629302340,
            "moonset": 1629243780,
            "moon_phase": 0.35,
            "temp": {"day": 25.41, "min": 23.11, "max": 25.79, "night": 23.18, "eve": 24.33, "morn": 23.66},
            "feels_like": {"day": 25.86, "night": 23.59, "eve": 24.75, "morn": 24.01},
            "pressure": 1010,
            "humidity": 71,
            "dew_point": 19.11,
            "wind_speed": 3.09,
            "wind_deg": 104,
            "wind_gust": 3.41,
            "weather": [{"id": 500, "main": "Rain", "description": "light rain", "icon": "10d"}],
            "clouds": 7,
            "pop": 0.33,
            "rain": 0.21,
            "uvi": 9,
        },
        {
            "dt": 1629370800,
            "sunrise": 1629348055,
            "sunset": 1629397786,
            "moonrise": 1629392280,
            "moonset": 1629333600,
            "moon_phase": 0.39,
            "temp": {"day": 24.85, "min": 21.71, "max": 24.91, "night": 23.23, "eve": 23.78, "morn": 22.04},
            "feels_like": {"day": 25.06, "night": 23.46, "eve": 23.99, "morn": 21.89},
            "pressure": 1006,
            "humidity": 64,
            "dew_point": 16.89,
            "wind_speed": 4.98,
            "wind_deg": 186,
            "wind_gust": 5.55,
            "weather": [{"id": 803, "main": "Clouds", "description": "broken clouds", "icon": "04d"}],
            "clouds": 51,
            "pop": 0.15,
            "uvi": 9,
        },
        {
            "dt": 1629457200,
            "sunrise": 1629434523,
            "sunset": 1629484091,
            "moonrise": 1629481560,
            "moonset": 1629424020,
            "moon_phase": 0.43,
            "temp": {"day": 25.09, "min": 22.89, "max": 25.1, "night": 23.16, "eve": 24.3, "morn": 23.09},
            "feels_like": {"day": 25.22, "night": 23.41, "eve": 24.51, "morn": 23.15},
            "pressure": 1013,
            "humidity": 60,
            "dew_point": 16.16,
            "wind_speed": 3.38,
            "wind_deg": 183,
            "wind_gust": 3.56,
            "weather": [{"id": 800, "main": "Clear", "description": "clear sky", "icon": "01d"}],
            "clouds": 9,
            "pop": 0.01,
            "uvi": 9,
        },
    ],
}


def validate_date_func(func, field):
    """Support function to validate date."""
    ocad = OneCallApiDaily(LAT, LON, KEY)
    ocad._rawdata = RAW_DATA_DAILY
    # case greater than
    with pytest.raises(ValueError):
        func(8)
    # case lesser than
    with pytest.raises(ValueError):
        func(-1)
    # nominal cases value by value
    for idx in range(7):
        assert RAW_DATA_DAILY["daily"][idx][field] == func(idx, 1, False)
    # nominal cases all values at once
    values = func(idx, 1, True)
    for idx in range(7):
        assert RAW_DATA_DAILY["daily"][idx][field] == values[idx]


def validate_value_func(func, field):
    """Support function to validate value."""
    ocad = OneCallApiDaily(LAT, LON, KEY)
    ocad._rawdata = RAW_DATA_DAILY
    # case greater than
    with pytest.raises(ValueError):
        func(8)
    # case lesser than
    with pytest.raises(ValueError):
        func(-1)
    # nominal cases value by value
    for idx in range(7):
        assert RAW_DATA_DAILY["daily"][idx][field] == func(idx, False)
    # nominal cases all values at once
    values = func(idx, True)
    for idx in range(7):
        assert RAW_DATA_DAILY["daily"][idx][field] == values[idx]


def validate_temp_func(func, group, field):
    """Support function to validate temperature."""
    ocad = OneCallApiDaily(LAT, LON, KEY)
    ocad._rawdata = RAW_DATA_DAILY
    # case greater than
    with pytest.raises(ValueError):
        func(8)
    # case lesser than
    with pytest.raises(ValueError):
        func(-1)
    # nominal cases value by value
    for idx in range(7):
        assert RAW_DATA_DAILY["daily"][idx][group][field] == func(idx, False)
    # nominal cases all values at once
    values = func(idx, True)
    for idx in range(7):
        assert RAW_DATA_DAILY["daily"][idx][group][field] == values[idx]


def validate_weather_func(func, field):
    """Support function to validate weather."""
    ocad = OneCallApiDaily(LAT, LON, KEY)
    ocad._rawdata = RAW_DATA_DAILY
    # case greater than
    with pytest.raises(ValueError):
        func(8)
    # case lesser than
    with pytest.raises(ValueError):
        func(-1)
    # nominal cases value by value
    for idx in range(7):
        assert RAW_DATA_DAILY["daily"][idx]["weather"][0][field] == func(idx, False)
    # nominal cases all values at once
    values = func(idx, True)
    for idx in range(7):
        assert RAW_DATA_DAILY["daily"][idx]["weather"][0][field] == values[idx]


def test_0000():
    """Test: validate constructor nominal case."""
    ocad = OneCallApiDaily(LAT, LON, KEY)
    assert ocad.lat == LAT
    assert ocad.lon == LON
    assert ocad.key == KEY
    assert ocad.exc == EXC


def test_0001():
    """Test: validate method raw_data_daily."""
    ocad = OneCallApiDaily(LAT, LON, KEY)
    ocad._rawdata = RAW_DATA_DAILY
    assert ocad.raw_data_daily() == RAW_DATA_DAILY["daily"]


def test_0002():
    """Test: validate method data_time."""
    ocad = OneCallApiDaily(LAT, LON, KEY)
    ocad._rawdata = RAW_DATA_DAILY
    validate_date_func(ocad.data_time, "dt")


def test_0003():
    """Test: validate method sunrise."""
    ocad = OneCallApiDaily(LAT, LON, KEY)
    ocad._rawdata = RAW_DATA_DAILY
    validate_date_func(ocad.sunrise, "sunrise")


def test_0004():
    """Test: validate method sunset."""
    ocad = OneCallApiDaily(LAT, LON, KEY)
    ocad._rawdata = RAW_DATA_DAILY
    validate_date_func(ocad.sunset, "sunset")


def test_0005():
    """Test: validate method moonrise."""
    ocad = OneCallApiDaily(LAT, LON, KEY)
    ocad._rawdata = RAW_DATA_DAILY
    validate_date_func(ocad.moonrise, "moonrise")


def test_0006():
    """Test: validate method moonset."""
    ocad = OneCallApiDaily(LAT, LON, KEY)
    ocad._rawdata = RAW_DATA_DAILY
    validate_date_func(ocad.moonset, "moonset")


def test_0007():
    """Test: validate method pressure."""
    ocad = OneCallApiDaily(LAT, LON, KEY)
    ocad._rawdata = RAW_DATA_DAILY
    validate_value_func(ocad.pressure, "pressure")


def test_0008():
    """Test: validate method humidity."""
    ocad = OneCallApiDaily(LAT, LON, KEY)
    ocad._rawdata = RAW_DATA_DAILY
    validate_value_func(ocad.humidity, "humidity")


def test_0009():
    """Test: validate method dew_point."""
    ocad = OneCallApiDaily(LAT, LON, KEY)
    ocad._rawdata = RAW_DATA_DAILY
    validate_value_func(ocad.dew_point, "dew_point")


def test_0010():
    """Test: validate method wind_speed."""
    ocad = OneCallApiDaily(LAT, LON, KEY)
    ocad._rawdata = RAW_DATA_DAILY
    validate_value_func(ocad.wind_speed, "wind_speed")


def test_0011():
    """Test: validate method wind_deg."""
    ocad = OneCallApiDaily(LAT, LON, KEY)
    ocad._rawdata = RAW_DATA_DAILY
    validate_value_func(ocad.wind_deg, "wind_deg")


def test_0012():
    """Test: validate method wind_gust."""
    ocad = OneCallApiDaily(LAT, LON, KEY)
    ocad._rawdata = RAW_DATA_DAILY
    validate_value_func(ocad.wind_gust, "wind_gust")


def test_0013():
    """Test: validate method clouds."""
    ocad = OneCallApiDaily(LAT, LON, KEY)
    ocad._rawdata = RAW_DATA_DAILY
    validate_value_func(ocad.clouds, "clouds")


def test_0014():
    """Test: validate method pop."""
    ocad = OneCallApiDaily(LAT, LON, KEY)
    ocad._rawdata = RAW_DATA_DAILY
    validate_value_func(ocad.pop, "pop")


def test_0015():
    """Test: validate method uvi."""
    ocad = OneCallApiDaily(LAT, LON, KEY)
    ocad._rawdata = RAW_DATA_DAILY
    validate_value_func(ocad.uvi, "uvi")


def test_0016():
    """Test: validate method temp_min."""
    ocad = OneCallApiDaily(LAT, LON, KEY)
    ocad._rawdata = RAW_DATA_DAILY
    validate_temp_func(ocad.temp_min, "temp", "min")


def test_0017():
    """Test: validate method temp_max."""
    ocad = OneCallApiDaily(LAT, LON, KEY)
    ocad._rawdata = RAW_DATA_DAILY
    validate_temp_func(ocad.temp_max, "temp", "max")


def test_0018():
    """Test: validate method temp_day."""
    ocad = OneCallApiDaily(LAT, LON, KEY)
    ocad._rawdata = RAW_DATA_DAILY
    validate_temp_func(ocad.temp_day, "temp", "day")


def test_0019():
    """Test: validate method temp_night."""
    ocad = OneCallApiDaily(LAT, LON, KEY)
    ocad._rawdata = RAW_DATA_DAILY
    validate_temp_func(ocad.temp_night, "temp", "night")


def test_0020():
    """Test: validate method temp_eve."""
    ocad = OneCallApiDaily(LAT, LON, KEY)
    ocad._rawdata = RAW_DATA_DAILY
    validate_temp_func(ocad.temp_eve, "temp", "eve")


def test_0021():
    """Test: validate method temp_morn."""
    ocad = OneCallApiDaily(LAT, LON, KEY)
    ocad._rawdata = RAW_DATA_DAILY
    validate_temp_func(ocad.temp_morn, "temp", "morn")


def test_0022():
    """Test: validate method feels_like_day."""
    ocad = OneCallApiDaily(LAT, LON, KEY)
    ocad._rawdata = RAW_DATA_DAILY
    validate_temp_func(ocad.feels_like_day, "feels_like", "day")


def test_0023():
    """Test: validate method feels_like_night."""
    ocad = OneCallApiDaily(LAT, LON, KEY)
    ocad._rawdata = RAW_DATA_DAILY
    validate_temp_func(ocad.feels_like_night, "feels_like", "night")


def test_0024():
    """Test: validate method feels_like_eve."""
    ocad = OneCallApiDaily(LAT, LON, KEY)
    ocad._rawdata = RAW_DATA_DAILY
    validate_temp_func(ocad.feels_like_eve, "feels_like", "eve")


def test_0025():
    """Test: validate method feels_like_morn."""
    ocad = OneCallApiDaily(LAT, LON, KEY)
    ocad._rawdata = RAW_DATA_DAILY
    validate_temp_func(ocad.feels_like_morn, "feels_like", "morn")


def test_0026():
    """Test: validate method weather_condition_id."""
    ocad = OneCallApiDaily(LAT, LON, KEY)
    ocad._rawdata = RAW_DATA_DAILY
    validate_weather_func(ocad.weather_condition_id, "id")


def test_0027():
    """Test: validate method weather_condition_main."""
    ocad = OneCallApiDaily(LAT, LON, KEY)
    ocad._rawdata = RAW_DATA_DAILY
    validate_weather_func(ocad.weather_condition_main, "main")


def test_0028():
    """Test: validate method weather_condition_description."""
    ocad = OneCallApiDaily(LAT, LON, KEY)
    ocad._rawdata = RAW_DATA_DAILY
    validate_weather_func(ocad.weather_condition_description, "description")


def test_0029():
    """Test: validate method weather_condition_icon."""
    ocad = OneCallApiDaily(LAT, LON, KEY)
    ocad._rawdata = RAW_DATA_DAILY
    validate_weather_func(ocad.weather_condition_icon, "icon")
