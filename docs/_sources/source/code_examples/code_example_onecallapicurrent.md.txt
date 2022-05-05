# Process One Call Api response for Current data

This functionality allows to process One Call Api response for Current data.

```python
from pocar.OneCallApiCurrent import OneCallApiCurrent

# CONSTANT DATA
LAT = 45.1234
LON = 1.2345
KEY = "abcdef1234567890abcdef1234567890"

def func_current()
    # 1. Create OneCallApi Current object
    ocac = OneCallApiCurrent(LAT, LON, KEY)

    # 2. Update Open Weather data for One Call Api
    ocac.update_data()

    # 3. Work on processed data
    print("One Call Api configuration: \n", ocac.config() )

    print("One Call Api configured latitude value : ", ocac.lat() )
    print("One Call Api configured longitude value: ", ocac.lon() )
    print("One Call Api configured API Key value  : ", ocac.key() )
    print("One Call Api configured excluded value : ", ocac.exc() )

    print("One Call Api response raw data full   :\n", ocac.raw_data() )
    print("One Call Api response raw data current:\n", ocac.raw_data_current() )

    print("One Call Api response, timezone       : ", ocac.timezone() )
    print("One Call Api response, timezone_offset: ", ocac.timezone_offset() )
    print("One Call Api data timestamp           : ", ocac.timestamp() )

    print("One Call Api response, current time                 : ", ocac.data_time() )
    print("One Call Api response, sunrise time                 : ", ocac.sunrise() )
    print("One Call Api response, sunset time                  : ", ocac.sunset() )
    print("One Call Api response, temperature                  : ", ocac.temperature() )
    print("One Call Api response, temperature feel             : ", ocac.temperature_feels_like() )
    print("One Call Api response, pressure                     : ", ocac.pressure() )
    print("One Call Api response, humidity                     : ", ocac.humidity() )
    print("One Call Api response, dew point                    : ", ocac.dew_point() )
    print("One Call Api response, clouds                       : ", ocac.clouds() )
    print("One Call Api response, uv index                     : ", ocac.uvi() )
    print("One Call Api response, visibility                   : ", ocac.visibility() )
    print("One Call Api response, wind speed                   : ", ocac.wind_speed() )
    print("One Call Api response, wind gust                    : ", ocac.wind_gust() )
    print("One Call Api response, wind degrees                 : ", ocac.wind_deg() )
    print("One Call Api response, rain volume                  : ", ocac.rain_volume() )
    print("One Call Api response, snow volume                  : ", ocac.snow_volume() )
    print("One Call Api response, weather condition id         : ", ocac.weather_condition_id() )
    print("One Call Api response, weather condition main       : ", ocac.weather_condition_main() )
    print("One Call Api response, weather condition description: ", ocac.weather_condition_description() )
    print("One Call Api response, weather condition icon       : ", ocac.weather_condition_icon() )
```
