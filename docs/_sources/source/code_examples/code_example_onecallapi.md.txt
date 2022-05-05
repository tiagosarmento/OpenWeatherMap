# Process One Call Api base response

This functionality allows to process One Call Api response at a base level.
Here the user will have access to response header fields and response raw data as a dictionary.

```python
from pocar.OneCallApi import OneCallApi

# CONSTANT DATA
LAT = 45.1234
LON = 1.2345
KEY = "abcdef1234567890abcdef1234567890"
EXC = ""

def func_base()
    # 1. Create OneCallApi object
    oca = OneCallApi(LAT, LON, KEY, EXC)

    # 2. Update Open Weather data for One Call Api
    oca.update_data()

    # 3. Work on processed data
    print("One Call Api configuration: \n", oca.config() )

    print("One Call Api configured latitude value : ", oca.lat() )
    print("One Call Api configured longitude value: ", oca.lon() )
    print("One Call Api configured API Key value  : ", oca.key() )
    print("One Call Api configured excluded value : ", oca.exc() )

    print("One Call Api response raw data: \n", oca.raw_data() )

    print("One Call Api response, timezone       : ", oca.timezone() )
    print("One Call Api response, timezone offset: ", oca.timezone_offset() )
    print("One Call Api data timestamp           : ", oca.timestamp() )
```
