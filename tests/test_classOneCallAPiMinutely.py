from pocar.OneCallApiMinutely import OneCallApiMinutely
import pytest

# CONSTANT DATA
LAT = 45.1234
LON = 1.2345
KEY = "abcdef1234567890abcdef1234567890"
EXC = "current,daily,hourly,alerts"
URL = f"https://api.openweathermap.org/data/2.5/onecall?lat={LAT}&lon={LON}&exclude={EXC}&units=metric&appid={KEY}"

RAW_DATA_MINUTELY = {
    "lat": 43.5832,
    "lon": 7.108,
    "timezone": "Europe/Paris",
    "timezone_offset": 7200,
    "minutely": [
        {"dt": 1628606160, "precipitation": 0},
        {"dt": 1628606220, "precipitation": 1},
        {"dt": 1628606280, "precipitation": 2},
        {"dt": 1628606340, "precipitation": 3},
        {"dt": 1628606400, "precipitation": 4},
        {"dt": 1628606460, "precipitation": 5},
        {"dt": 1628606520, "precipitation": 6},
        {"dt": 1628606580, "precipitation": 7},
        {"dt": 1628606640, "precipitation": 8},
        {"dt": 1628606700, "precipitation": 9},
        {"dt": 1628606760, "precipitation": 10},
        {"dt": 1628606820, "precipitation": 11},
        {"dt": 1628606880, "precipitation": 12},
        {"dt": 1628606940, "precipitation": 13},
        {"dt": 1628607000, "precipitation": 14},
        {"dt": 1628607060, "precipitation": 15},
        {"dt": 1628607120, "precipitation": 16},
        {"dt": 1628607180, "precipitation": 17},
        {"dt": 1628607240, "precipitation": 18},
        {"dt": 1628607300, "precipitation": 19},
        {"dt": 1628607360, "precipitation": 20},
        {"dt": 1628607420, "precipitation": 21},
        {"dt": 1628607480, "precipitation": 22},
        {"dt": 1628607540, "precipitation": 23},
        {"dt": 1628607600, "precipitation": 24},
        {"dt": 1628607660, "precipitation": 25},
        {"dt": 1628607720, "precipitation": 26},
        {"dt": 1628607780, "precipitation": 27},
        {"dt": 1628607840, "precipitation": 28},
        {"dt": 1628607900, "precipitation": 29},
        {"dt": 1628607960, "precipitation": 30},
        {"dt": 1628608020, "precipitation": 31},
        {"dt": 1628608080, "precipitation": 32},
        {"dt": 1628608140, "precipitation": 33},
        {"dt": 1628608200, "precipitation": 34},
        {"dt": 1628608260, "precipitation": 35},
        {"dt": 1628608320, "precipitation": 36},
        {"dt": 1628608380, "precipitation": 37},
        {"dt": 1628608440, "precipitation": 38},
        {"dt": 1628608500, "precipitation": 39},
        {"dt": 1628608560, "precipitation": 40},
        {"dt": 1628608620, "precipitation": 41},
        {"dt": 1628608680, "precipitation": 42},
        {"dt": 1628608740, "precipitation": 43},
        {"dt": 1628608800, "precipitation": 44},
        {"dt": 1628608860, "precipitation": 45},
        {"dt": 1628608920, "precipitation": 46},
        {"dt": 1628608980, "precipitation": 47},
        {"dt": 1628609040, "precipitation": 48},
        {"dt": 1628609100, "precipitation": 49},
        {"dt": 1628609160, "precipitation": 50},
        {"dt": 1628609220, "precipitation": 51},
        {"dt": 1628609280, "precipitation": 52},
        {"dt": 1628609340, "precipitation": 53},
        {"dt": 1628609400, "precipitation": 54},
        {"dt": 1628609460, "precipitation": 55},
        {"dt": 1628609520, "precipitation": 56},
        {"dt": 1628609580, "precipitation": 57},
        {"dt": 1628609640, "precipitation": 58},
        {"dt": 1628609700, "precipitation": 59},
        {"dt": 1628609760, "precipitation": 60},
    ],
}


# Test: validate constructor nominal case
def test_0000():
    ocam = OneCallApiMinutely(LAT, LON, KEY)
    assert ocam.lat == LAT
    assert ocam.lon == LON
    assert ocam.key == KEY
    assert ocam.exc == EXC


# Test: validate method raw data minutely
def test_0001():
    ocam = OneCallApiMinutely(LAT, LON, KEY)
    ocam._rawdata = RAW_DATA_MINUTELY
    assert ocam.raw_data_minutely() == RAW_DATA_MINUTELY["minutely"]


# Test: validate method precipitation
def test_0002():
    ocam = OneCallApiMinutely(LAT, LON, KEY)
    ocam._rawdata = RAW_DATA_MINUTELY
    # case greater than
    with pytest.raises(ValueError):
        ocam.precipitation(61)
    # case lesser than
    with pytest.raises(ValueError):
        ocam.precipitation(-1)
    # nominal cases value by value
    for idx in range(61):
        assert RAW_DATA_MINUTELY["minutely"][idx]["precipitation"] == ocam.precipitation(idx, False)
    # nominal cases all values at once
    values = ocam.precipitation(idx, True)
    for idx in range(61):
        assert RAW_DATA_MINUTELY["minutely"][idx]["precipitation"] == values[idx]


# Test: validate method precipitation
def test_0003():
    ocam = OneCallApiMinutely(LAT, LON, KEY)
    ocam._rawdata = RAW_DATA_MINUTELY
    # case greater than
    with pytest.raises(ValueError):
        ocam.data_time(61)
    # case lesser than
    with pytest.raises(ValueError):
        ocam.data_time(-1)
    # nominal cases value by value
    for idx in range(61):
        assert RAW_DATA_MINUTELY["minutely"][idx]["dt"] == ocam.data_time(idx, 1, False)
    # nominal cases all values at once
    values = ocam.data_time(idx, 1, True)
    for idx in range(61):
        assert RAW_DATA_MINUTELY["minutely"][idx]["dt"] == values[idx]
