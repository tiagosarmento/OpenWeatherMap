# Process One Call Api response for Daily data

This functionality allows to process One Call Api response for Daily data.
The Daily data holds the weather forecast for the next 7 days in a daily basis (available data is: today weather forecast, plus next 7 days).

```python
from pocar.OneCallApiDaily import OneCallApiDaily

# CONSTANT DATA
LAT = 45.1234
LON = 1.2345
KEY = "abcdef1234567890abcdef1234567890"

def func_daily()
    # 1. Create OneCallApi Daily object
    ocad = OneCallApiDaily(LAT, LON, KEY)

    # 2. Update Open Weather data for One Call Api
    ocad.updateData()

    # 3. Work on processed data
    print("One Call Api configuration: \n", ocad.config() )

    print("One Call Api configured latitude value : ", ocad.lat() )
    print("One Call Api configured longitude value: ", ocad.lon() )
    print("One Call Api configured API Key value  : ", ocad.key() )
    print("One Call Api configured excluded value : ", ocad.exc() )

    print("One Call Api response raw data full:  \n", ocad.raw_data() )
    print("One Call Api response raw data current\n", ocad.raw_data_daily() )

    print("One Call Api response, timezone       : ", ocad.timezone() )
    print("One Call Api response, timezone_offset: ", ocad.timezone_offset() )
    print("One Call Api data timestamp           : ", ocad.timestamp() )

    print("One Call Api response, current time                 : ", ocad.data_time() )
    print("One Call Api response, sunrise time                 : ", ocad.sunrise() )
    print("One Call Api response, sunset time                  : ", ocad.sunset() )
    print("One Call Api response, moonrise time                : ", ocad.moonrise() )
    print("One Call Api response, moonset time                 : ", ocad.moonset() )
    print("One Call Api response, temperature (day)            : ", ocad.temp_day() )
    print("One Call Api response, temperature (min)            : ", ocad.temp_min() )
    print("One Call Api response, temperature (max)            : ", ocad.temp_max() )
    print("One Call Api response, temperature (night)          : ", ocad.temp_night() )
    print("One Call Api response, temperature (evening)        : ", ocad.temp_eve() )
    print("One Call Api response, temperature (morning)        : ", ocad.temp_morn() )
    print("One Call Api response, temperature feel (day)       : ", ocad.feels_like_day() )
    print("One Call Api response, temperature feel (night)     : ", ocad.feels_like_night() )
    print("One Call Api response, temperature feel (evening)   : ", ocad.feels_like_eve() )
    print("One Call Api response, temperature feel (morning)   : ", ocad.feels_like_morn() )
    print("One Call Api response, pressure                     : ", ocad.pressure() )
    print("One Call Api response, humidity                     : ", ocad.humidity() )
    print("One Call Api response, dew point                    : ", ocad.dew_point() )
    print("One Call Api response, wind speed                   : ", ocad.wind_speed() )
    print("One Call Api response, wind gust                    : ", ocad.wind_gust() )
    print("One Call Api response, wind degrees                 : ", ocad.wind_deg() )
    print("One Call Api response, clouds                       : ", ocad.clouds() )
    print("One Call Api response, precipitation                : ", ocad.pop() )
    print("One Call Api response, uvi                          : ", ocad.uvi() )
    print("One Call Api response, weather condition id         : ", ocad.weather_condition_id() )
    print("One Call Api response, weather condition main       : ", ocad.weather_condition_main() )
    print("One Call Api response, weather condition description: ", ocad.weather_condition_description() )
    print("One Call Api response, weather condition icon       : ", ocad.weather_condition_icon() )
```
