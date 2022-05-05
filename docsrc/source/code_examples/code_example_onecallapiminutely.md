# Process One Call Api response for Minutely data

This functionality allows to process One Call Api response for Minutely data.
The Minutely data holds the precipitation forecast for the next 60 minutes in a minute basis (available data is: current minute precipitation forecast, plus for next 60 minutes)

```python
from pocar.OneCallApiMinutely import OneCallApiMinutely

# CONSTANT DATA
LAT = 45.1234
LON = 1.2345
KEY = "abcdef1234567890abcdef1234567890"

def func_minutely()
    # 1. Create OneCallApi Minutely object
    ocam = OneCallApiMinutely(LAT, LON, KEY)

    # 2. Update Open Weather data for One Call Api
    ocam.update_data()

    # 3. Work on processed data
    print("One Call Api configuration: \n", ocam.config() )

    print("One Call Api configured latitude value : ", ocam.lat() )
    print("One Call Api configured longitude value: ", ocam.lon() )
    print("One Call Api configured API Key value  : ", ocam.key() )
    print("One Call Api configured excluded value : ", ocam.exc() )

    print("One Call Api response raw data full:  \n", ocam.raw_data() )
    print("One Call Api response raw data current\n", ocam.raw_data_minutely() )

    print("One Call Api response, timezone       : ", ocam.timezone() )
    print("One Call Api response, timezone_offset: ", ocam.timezone_offset() )
    print("One Call Api data timestamp           : ", ocam.timestamp() )

    print("One Call Api response, current time : ", ocam.data_time() )
    print("One Call Api response, precipitation: ", ocam.precipitation() )
```
