# Process One Call Api response for Alerts data

This functionality allows to process One Call Api response for Alerts data.
The Alerts data holds the National weather alerts data from major national weather warning systems.

```python
from pocar.OneCallApiAlerts import OneCallApiAlerts

# CONSTANT DATA
LAT = 45.1234
LON = 1.2345
KEY = "abcdef1234567890abcdef1234567890"

def func_alerts()
    # 1. Create OneCallApi Alerts object
    ocaa = OneCallApiAlerts(LAT, LON, KEY)

    # 2. Update Open Weather data for One Call Api
    ocaa.update_data()

    # 3. Work on processed data
    print("One Call Api configuration: \n", ocaa.config() )

    print("One Call Api configured latitude value : ", ocaa.lat() )
    print("One Call Api configured longitude value: ", ocaa.lon() )
    print("One Call Api configured API Key value  : ", ocaa.key() )
    print("One Call Api configured excluded value : ", ocaa.exc() )

    print("One Call Api response raw data full:  \n", ocaa.raw_data() )
    print("One Call Api response raw data current\n", ocaa.raw_data_alerts() )

    print("One Call Api response, timezone       : ", ocaa.timezone() )
    print("One Call Api response, timezone_offset: ", ocaa.timezone_offset() )
    print("One Call Api data timestamp           : ", ocaa.timestamp() )

    print("One Call Api response, sender name: ", ocaa.sender_name() )
    print("One Call Api response, event      : ", ocaa.event() )
    print("One Call Api response, start date : ", ocaa.start_dt() )
    print("One Call Api response, end date   : ", ocaa.end_dt() )
    print("One Call Api response, description: ", ocaa.description() )
    print("One Call Api response, tags       : ", ocaa.tags() )
```
