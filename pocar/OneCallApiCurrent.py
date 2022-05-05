"""This module provides a base class to handle One Call Api response for Current from OpenWeatherMap."""
import logging
from datetime import datetime

import requests

from pocar.OneCallApi import OneCallApi


# Uncomment this line to suppress warning message due to:
#    InsecureRequestWarning: Unverified HTTPS request is being made.
#    Adding certificate verification is strongly advised.
#    See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
# We get this warning because an HTTP GET request is made with SSL verification disabled
requests.packages.urllib3.disable_warnings()

# Set local logger to the root logger, to inherit root settings
logger = logging.getLogger(__name__)


# Derived Class to handle Current weather data API response
class OneCallApiCurrent(OneCallApi):
    """
    Base Class to handle OneCallApi response for Alerts from OpenWeatherMap.

    This Class is derived from :class:`~pocar.OneCallAPi.OneCallAPi`

    :param lat: Geographical coordinates of the location (latitude)
    :type lat: float, range [-90; 90]

    :param lon: Geographical coordinates of the location (longitude)
    :type lon: float, range [-180; 180]

    :param key: The OpenWeatherMap One Call Api key value
    :type key: hex, 128-bit hash key
    """

    def __init__(self, lat, lon, key):
        """This is the constructor method."""
        super().__init__(lat, lon, key, "minutely,daily,hourly,alerts")

    def __is_data_available(self, field):
        """TBD."""
        value = False
        if ("current" in self._rawdata) and (field in self._rawdata["current"]):
            value = True
        return value

    def __extract_date_field(self, field, metrics=0):
        """TBD."""
        value = "N/A"
        if self.__is_data_available(field) is True:
            if metrics == 0:
                dt = datetime.fromtimestamp(self._rawdata["current"][field])
                value = f"{dt:%Y-%m-%d %H:%M:%S}"
            else:
                value = self._rawdata["current"][field]
        logger.debug("Value for %s is: %s", field, value)
        return value

    def __extract_value_field(self, field):
        """TBD."""
        value = "N/A"
        if self.__is_data_available(field) is True:
            value = self._rawdata["current"][field]
        logger.debug("Value for %s is: %s", field, value)
        return value

    def __extract_weather_field(self, field):
        """TBD."""
        value = "N/A"
        if self.__is_data_available("weather") is True:
            if field in self._rawdata["current"]["weather"][0]:
                value = self._rawdata["current"]["weather"][0][field]
        logger.debug("Value for %s is: %s", field, value)
        return value

    def raw_data_current(self):
        """
        | The raw_data_current method.

        | Returns field current of the variable :attr:`~pocar.OneCallAPi.OneCallAPi._raw_data`
        | This variable contains the One Call Api response for alerts raw data as a dictionary

        :return: raw data as a dictionary
        :rtype: dict
        """
        value = {}
        if "current" in self._rawdata:
            value = self._rawdata["current"]
        return value

    def data_time(self, metrics=0):
        """
        | The data_time method.

        | Returns the value for dt from One Call Api response
        | This is the Time when current data was acquired
        | One Call Api response field is: `current.dt`

        :param metrics: option to select metrics type, 0 = DATE string, UNIX UTC otherwise
        :type metrics: int, optional

        :return: Current time
        :rtype: date if metrics is 0 or int otherwise
        """
        return self.__extract_date_field("dt", metrics)

    def sunrise(self, metrics=0):
        """
        | The sunrise method.

        | Returns the value for sunrise from One Call Api response
        | This is the sunrise time for current
        | One Call Api response field is: `current.sunrise`

        :param metrics: option to select metrics type, 0 = DATE string, UNIX UTC otherwise
        :type metrics: int, optional

        :return: Sunrise time
        :rtype: date if metrics is 0 or int otherwise
        """
        return self.__extract_date_field("sunrise", metrics)

    def sunset(self, metrics=0):
        """
        | The sunset method.

        | Returns the value for sunset from One Call Api response
        | This is the sunset time for current
        | One Call Api response field is: `current.sunset`

        :param metrics: option to select metrics type, 0 = DATE string, UNIX UTC otherwise
        :type metrics: int, optional

        :return: Sunset time
        :rtype: date if metrics is 0 or int otherwise
        """
        return self.__extract_date_field("sunset", metrics)

    def temperature(self):
        """
        | The temperature method.

        | Returns the value for temp from One Call Api response
        | One Call Api response field is: `current.temp`

        :return: Temperature, C
        :rtype: float
        """
        return self.__extract_value_field("temp")

    def temperature_feels_like(self):
        """
        | The temperature_feels_like method.

        | Returns the value for feels_like from One Call Api response
        | One Call Api response field is: `current.feels_like`

        :return: Temperature feeling (the human perception of weather), C
        :rtype: float
        """
        return self.__extract_value_field("feels_like")

    def pressure(self):
        """
        | The pressure method.

        | Returns the value for pressure from One Call Api response
        | One Call Api response field is: `current.pressure`

        :return: Atmospheric pressure on the sea level, hPa
        :rtype: int
        """
        return self.__extract_value_field("pressure")

    def humidity(self):
        """
        | The humidity method.

        | Returns the value for humidity from One Call Api response
        | One Call Api response field is: `current.humidity`

        :return: Humidity, %
        :rtype: int
        """
        return self.__extract_value_field("humidity")

    def dew_point(self):
        """
        | The dew_point method.

        | Returns the value for dew_point from One Call Api response
        | One Call Api response field is: `current.dew_point`
        | Atmospheric temperature (varying according to pressure and humidity)
        | below which water droplets begin to condense and dew can form.

        :return: Temperature, C
        :rtype: float
        """
        return self.__extract_value_field("dew_point")

    def clouds(self):
        """
        | The clouds method.

        | Returns the value for clouds from One Call Api response
        | One Call Api response field is: `current.clouds`

        :return: Cloudiness, %
        :rtype: int
        """
        return self.__extract_value_field("clouds")

    def uvi(self):
        """
        | The uvi method.

        | Returns the value for uvi from One Call Api response
        | One Call Api response field is: `current.uvi`

        :return: UV index
        :rtype: float
        """
        return self.__extract_value_field("uvi")

    def visibility(self):
        """
        | The visibility method.

        | Returns the value for visibility from One Call Api response
        | One Call Api response field is: `current.visibility`

        :return: Average visibility, metres
        :rtype: int
        """
        return self.__extract_value_field("visibility")

    def wind_speed(self):
        """
        | The wind_speed method.

        | Returns the value for wind_speed from One Call Api response
        | One Call Api response field is: `current.wind_speed`

        :return: Wind speed, m/s
        :rtype: float
        """
        return self.__extract_value_field("wind_speed")

    def wind_gust(self):
        """
        | The wind_gust method.

        | Returns the value for wind_gust from One Call Api response
        | One Call Api response field is: `current.wind_gust`
        | This value is not available for all locations.

        :return: Wind gust, m/s
        :rtype: float
        """
        return self.__extract_value_field("wind_gust")

    def wind_deg(self):
        """
        | The wind_deg method.

        | Returns the value for wind_deg from One Call Api response
        | One Call Api response field is: `current.wind_deg`

        :return: Wind direction, degrees
        :rtype: int
        """
        return self.__extract_value_field("wind_deg")

    def rain_volume(self):
        """
        | The rain_volume method.

        | Returns the value for rain.1h from One Call Api response
        | One Call Api response field is: `current.rain.1h`
        | This value is not available for all locations.

        :return: Rain volume for last hour, mm
        :rtype: int
        """
        value = "N/A"
        if self.__is_data_available("rain") is True:
            if "1h" in self._rawdata["current"]["rain"]:
                value = self._rawdata["current"]["rain"]["1h"]
        return value

    def snow_volume(self):
        """
        | The snow_volume method.

        | Returns the value for snow.1h from One Call Api response
        | One Call Api response field is: `current.snow.1h`
        | This value is not available for all locations.

        :return: Snow volume for last hour, mm
        :rtype: int
        """
        value = "N/A"
        if self.__is_data_available("snow") is True:
            if "1h" in self._rawdata["current"]["snow"]:
                value = self._rawdata["current"]["snow"]["1h"]
        return value

    def weather_condition_id(self):
        """
        | The weather_condition_id method.

        | Returns the value for weather.id from One Call Api response
        | One Call Api response field is: `current.weather.id`

        :return: Weather condition id
        :rtype: int
        """
        return self.__extract_weather_field("id")

    def weather_condition_main(self):
        """
        | The weather_condition_main method.

        | Returns the value for weather.main from One Call Api response
        | One Call Api response field is: `current.weather.main`

        :return: Group of weather parameters (Rain, Snow, Extreme etc.)
        :rtype: str
        """
        return self.__extract_weather_field("main")

    def weather_condition_description(self):
        """
        | The weather_condition_description method.

        | Returns the value for weather.description from One Call Api response
        | One Call Api response field is: `current.weather.description`

        :return: Weather condition within the group
        :rtype: str
        """
        return self.__extract_weather_field("description")

    def weather_condition_icon(self):
        """
        | The weather_condition_icon method.

        | Returns the value for weather.icon from One Call Api response
        | One Call Api response field is: `current.weather.icon`
        | The icon can be retrieve from: http://openweathermap.org/img/wn/<icon_id>@2x.png

        :return: Weather icon id
        :rtype: str
        """
        return self.__extract_weather_field("icon")
