import openweathermap


def test_constructor():
    lat = 43.58
    lon = 7.10
    key = "1234567abcdefg"
    timeThrs = 120
    oca = openweathermap.OneCallApi(lat, lon, key, timeThrs)

    assert oca._lat == lat
    assert oca._lon == lon
    assert oca._key == key
    assert oca._timeThrs == timeThrs
    assert len(oca._ocadata) == 0
    assert oca._dataTime == 0
    assert oca._url == (
        f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}"
        f"&units=metric&appid={key}"
    )
