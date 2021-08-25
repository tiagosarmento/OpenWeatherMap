# Process One Call Api response for Hourly data

This functionality allows to process One Call Api response for Hourly data.
The Hourly data holds the weather forecast for the next 48 hours in a hourly basis (available data is: current hour weather forecast, plus for next 47 hours)

```python
from pocar.OneCallApiHourly import OneCallApiHourly

# CONSTANT DATA
LAT = 45.1234
LON = 1.2345
KEY = "abcdef1234567890abcdef1234567890"

def func_hourly()
    # 1. Create OneCallApi Hourly object
    ocah = OneCallApiHourly(LAT, LON, KEY)

    # 2. Update Open Weather data for One Call Api
    ocah.updateData()

    # 3. Work on processed data
    print("One Call Api configuration: \n", ocah.config() )

    print("One Call Api configured latitude value : ", ocah.lat() )
    print("One Call Api configured longitude value: ", ocah.lon() )
    print("One Call Api configured API Key value  : ", ocah.key() )
    print("One Call Api configured excluded value : ", ocah.exc() )

    print("One Call Api response raw data full:  \n", ocah.raw_data() )
    print("One Call Api response raw data current\n", ocah.raw_data_minutely() )

    print("One Call Api response, timezone       : ", ocah.timezone() )
    print("One Call Api response, timezone_offset: ", ocah.timezone_offset() )
    print("One Call Api data timestamp           : ", ocah.timestamp() )

    print("One Call Api response, current time                 : ", ocah.data_time() )
    print("One Call Api response, temperature                  : ", ocah.temp() )
    print("One Call Api response, temperature feel             : ", ocah.feels_like() )
    print("One Call Api response, pressure                     : ", ocah.pressure() )
    print("One Call Api response, humidity                     : ", ocah.humidity() )
    print("One Call Api response, dew point                    : ", ocah.dew_point() )
    print("One Call Api response, wind speed                   : ", ocah.wind_speed() )
    print("One Call Api response, wind gust                    : ", ocah.wind_gust() )
    print("One Call Api response, wind degrees                 : ", ocah.wind_deg() )
    print("One Call Api response, clouds                       : ", ocah.clouds() )
    print("One Call Api response, precipitation                : ", ocah.pop() )
    print("One Call Api response, uvi                          : ", ocah.uvi() )
    print("One Call Api response, weather condition id         : ", ocah.weather_condition_id() )
    print("One Call Api response, weather condition main       : ", ocah.weather_condition_main() )
    print("One Call Api response, weather condition description: ", ocah.weather_condition_description() )
    print("One Call Api response, weather condition icon       : ", ocah.weather_condition_icon() )
```
