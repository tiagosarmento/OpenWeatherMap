#!/usr/bin/env python3

# Begin of module OpenWeatherMap for OneCallApi response

import json
import logging
import requests
import time

from datetime import datetime


# Uncomment this line to suppress warning message due to:
#    InsecureRequestWarning: Unverified HTTPS request is being made.
#    Adding certificate verification is strongly advised.
#    See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
# We get this warning because an HTTP GET request is made with SSL verification disabled
requests.packages.urllib3.disable_warnings()

# Set local logger to the root logger, to inherit root settings
logger = logging.getLogger(__name__)


# Base Class to handle OneCallApi response from OpenWeatherMap
class OneCallApi:
    def __init__(self, lat, lon, key, exc=""):
        self.lat = lat
        self.lon = lon
        self.key = key
        self.exc = exc
        self._rawdata = dict()
        self._timestamp = 0
        self.__url = (
            f"https://api.openweathermap.org/data/2.5/onecall?lat={self._lat}&lon={self._lon}"
            f"&exclude={self._exc}&units=metric&appid={self._key}"
        )

    @property
    def lat(self):
        logger.debug("Get method for 'lat' attribute")
        return self._lat

    @lat.setter
    def lat(self, lat):
        logger.debug("Set method for 'lat' attribute")
        if lat < -90.0 or lat > 90.0:
            raise ValueError("The 'lat' argument must be within range [-90, 90]")
        else:
            self._lat = lat
            logger.debug("Set 'lat' value to: %s", self._lat)

    @property
    def lon(self):
        logger.debug("Get method for 'lon' attribute")
        return self._lon

    @lon.setter
    def lon(self, lon):
        logger.debug("Set method for 'lon' attribute")
        if lon < -180.0 or lon > 180.0:
            raise ValueError("The 'lon' argument must be within range [-180, 180]")
        else:
            self._lon = lon
            logger.debug("Set 'lon' value to: %s", self._lon)

    @property
    def key(self):
        logger.debug("Get method for 'key' attribute")
        return self._key

    @key.setter
    def key(self, key):
        logger.debug("Set method for 'key' attribute")
        # The 128-bit (16-byte) OpenWeatherMap hash key is represented as a sequence of 32 hexadecimal digits
        try:
            int(key, 16)
        except ValueError:
            logger.error(
                "The 'key' argument must be an hash value of 32 hexadecimal digits"
            )
            raise  # raise error for traceback access

        if len(key) != 32:
            raise ValueError("The 'key' argument must have a size of 32")
        else:
            self._key = key
            logger.debug("Set 'key' value to: %s", self._key)

    @property
    def exc(self):
        logger.debug("Get method for 'exc' attribute")
        return self._exc

    @exc.setter
    def exc(self, exc):
        logger.debug("Set method for 'exc' attribute")
        if len(exc) == 0:
            # the exclusion string can be empty, meaning that none of the OneCallAPi response are excluded
            # nothing to be done
            self._exc = exc
        elif any(True for char in exc if char in '@^! #%$&)(+*-="'):
            # the exclusion shall be a comma-delimited string (without spaces).
            # Allowed values are: current, minutely, hourly, daily and alerts
            raise ValueError(
                "The 'exc' argument must be a comma-delimited string (without spaces)"
            )
        else:
            # the exclusion shall contain specific words
            specWordList = ["current", "minutely", "hourly", "daily", "alerts"]
            excWordList = exc.split(",")
            for excWord in excWordList:
                if excWord in specWordList:
                    logger.debug("The 'exc' argument contains word: %s", excWord)
                else:
                    logger.error(
                        "The 'exc' argument contains an invalid word: %s", excWord
                    )
                    raise ValueError(
                        "The 'exc' argument must specific words: (current, minutely, hourly, daily, alerts)"
                    )
            self._exc = exc
        logger.debug("Set 'exc' value to: %s", self._exc)

    # Gets the configuration used to access OpenWeatherMap for OneCallApi.
    def config(self):
        conf_dict = dict(
            {
                "lat": self._lat,
                "lon": self._lon,
                "key": self._key,
                "exc": self._exc,
                "url": self.__url,
            }
        )
        logger.debug("Configuration to access OpenWeatherMap for OneCallApi: ")
        logger.debug("   Latitude       : %s", self._lat)
        logger.debug("   Longitude      : %s", self._lon)
        logger.debug("   Excluded parts : %s", self._exc)
        logger.debug("   API Key        : %s", self._key)
        logger.debug("   API url        : %s", self.__url)
        return conf_dict

    # Get OpenWeatherMap raw data from OneCallApi response. (full response)
    def raw_data(self):
        return self._rawdata

    # Get OpenWeatherMap data from OneCallApi
    # Data is stored as a dictionary in self._rawdata
    def __getData(self):
        is_data_updated = False
        req = requests.get(self.__url, verify=False)
        try:
            req.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            logger.warning(errh)
            # raise
        except requests.exceptions.ConnectionError as errc:
            logger.warning(errc)
            # raise
        except requests.exceptions.TimeoutError as errt:
            logger.warning(errt)
            # raise
        except requests.exceptions.RequestsException as err:
            logger.warning(err)
            # raise
        else:
            self._rawdata = req.json()
            logger.debug(
                "OneCallApi response, as json raw data:\n%s",
                json.dumps(self._rawdata, indent=2),
            )
            self._timestamp = time.time()
            logger.debug("OneCallApi response timestamp: %s", self._timestamp)
            is_data_updated = True
        return is_data_updated

    # Make an update of OpenWeatherMap data
    # Returns:
    #   True: if data successfuly updated
    #   False: if failed to update data
    def updateData(self):
        return self.__getData()

    # Get Timezone name for the requested location
    def timezone(self):
        value = ""
        if "timezone" in self._rawdata:
            value = self._rawdata["timezone"]
        return value

    # Get Timezone offset Shift in seconds of the requested location from UTC
    def timezone_offset(self):
        value = ""
        if "timezone_offset" in self._rawdata:
            value = self._rawdata["timezone_offset"]
        return value

    # Get timestamp of OpenWeatherMap data in seconds
    def timestamp(self):
        return self._timestamp


# Derived Class to handle Current weather data API response
class OneCallApiCurrent(OneCallApi):
    def __init__(self, lat, lon, key):
        super().__init__(
            lat, lon, key, "minutely,daily,hourly,alerts"
        )  # Init parent attributes

    def __is_data_available(self, field):
        value = False
        if ("current" in self._rawdata) and (field in self._rawdata["current"]):
            value = True
        return value

    def __extract_date_field(self, field, metrics=0):
        value = "N/A"
        if self.__is_data_available(field) is True:
            if metrics == 0:
                value = datetime.fromtimestamp(self._rawdata["current"][field])
            else:
                value = self._rawdata["current"][field]
        logger.debug("Value for %s is: %s", field, value)
        return value

    def __extract_value_field(self, field):
        value = "N/A"
        if self.__is_data_available(field) is True:
            value = self._rawdata["current"][field]
        logger.debug("Value for %s is: %s", field, value)
        return value

    def __extract_weather_field(self, field):
        value = "N/A"
        if self.__is_data_available("weather") is True:
            if field in self._rawdata["current"]["weather"][0]:
                value = self._rawdata["current"]["weather"][0][field]
        logger.debug("Value for %s is: %s", field, value)
        return value

    def raw_data_current(self):
        value = dict()
        if "current" in self._rawdata:
            value = self._rawdata["current"]
        return value

    # Get Current time, Unix, UTC
    # metrics defaults to 0: date in human readable format
    # any other value, date is represented as UNIX seconds
    def data_time(self, metrics=0):
        return self.__extract_date_field("dt", metrics)

    # Get Sunrise time, Unix, UTC
    def sunrise(self, metrics=0):
        return self.__extract_date_field("sunrise", metrics)

    # Get Sunset time, Unix, UTC
    def sunset(self, metrics=0):
        return self.__extract_date_field("sunset", metrics)

    # Get Current Temperature
    def temperature(self):
        return self.__extract_value_field("temp")

    # Get Current Temperature feel
    def temperature_feels_like(self):
        return self.__extract_value_field("feels_like")

    # Get Current Atmospheric pressure on the sea level, hPa
    def pressure(self):
        return self.__extract_value_field("pressure")

    # Get Current Humidity, %
    def humidity(self):
        return self.__extract_value_field("humidity")

    # Get Current Atmospheric temperature
    def dew_point(self):
        return self.__extract_value_field("dew_point")

    # Get Current Cloudiness, %
    def clouds(self):
        return self.__extract_value_field("clouds")

    # Get Current UV index
    def uvi(self):
        return self.__extract_value_field("uvi")

    # Get Current Average visibility, metres
    def visibility(self):
        return self.__extract_value_field("visibility")

    # Get Current Wind speed (m/s)
    def wind_speed(self):
        return self.__extract_value_field("wind_speed")

    # Get Current Wind gust (where available)
    def wind_gust(self):
        return self.__extract_value_field("wind_gust")

    # Get Current Wind direction, degrees (meteorological)
    def wind_deg(self):
        return self.__extract_value_field("wind_deg")

    # Get Current Rain volume for last hour, mm (where available)
    def rain_volume(self):
        value = "N/A"
        if self.__is_data_available("rain") is True:
            if "1h" in self._rawdata["current"]["rain"]:
                value = self._rawdata["current"]["rain"]["1h"]
        return value

    # Get Current Snow volume for last hour, mm (where available)
    def snow_volume(self):
        value = "N/A"
        if self.__is_data_available("snow") is True:
            if "1h" in self._rawdata["current"]["snow"]:
                value = self._rawdata["current"]["snow"]["1h"]
        return value

    # Get Current Weather condition id
    def weather_condition_id(self):
        return self.__extract_weather_field("id")

    # Get Group of weather parameters (Rain, Snow, Extreme etc.)
    def weather_condition_main(self):
        return self.__extract_weather_field("main")

    # Get Weather condition within the group (full list of weather conditions)
    def weather_condition_description(self):
        return self.__extract_weather_field("description")

    # Get Weather icon id. How to get icons
    #  http://openweathermap.org/img/wn/<icon_id>@2x.png
    def weather_condition_icon(self):
        return self.__extract_weather_field("icon")


# Derived Class to handle Minutely weather data API response
# Minutely holds the precipitation forecast for the next hour in a minutely basis
class OneCallApiMinutely(OneCallApi):
    def __init__(self, lat, lon, key):
        super().__init__(lat, lon, key)  # Init parent attributes
        self.__minutPrecDict = dict()

    # Gets 61 values: current + next 60 minutes
    def getMinutelyData(self, minute=0):
        self.updateData()
        if minute == 0:
            # gets the full dictionary data
            self.__minutPrecDict = self._rawdata["minutely"]
        else:
            # gets current time + minute precipitation forecast
            self.__minutPrecDict = self._rawdata["minutely"][minute]["precipitation"]
        return self.__minutPrecDict


# Derived Class to handle Hourly weather data API response
# Hourly holds the weather forecast for the next 48 hours in a hourly basis
class OneCallApiHourly(OneCallApi):
    def __init__(self, lat, lon, key):
        super().__init__(lat, lon, key)  # Init parent attributes
        self.__hourlyDict = dict()

    # Gets 48 values: weather for next 48 hours
    def getHourlyData(self, hour=0):
        self.updateData()
        self.__hourlyDict = self._rawdata["hourly"][hour]
        return self.__hourlyDict


# Derived Class to handle Daily weather data API response
# Daily holds the weather forecast for the next 7 days in a daily basis
class OneCallApiDaily(OneCallApi):
    def __init__(self, lat, lon, key):
        super().__init__(lat, lon, key)  # Init parent attributes
        self.__dailyDict = dict()

    # Gets 7 values: weather today + for next 7 days
    def getDailyData(self, day=0):
        self.updateData()
        self.__dailyDict = self._rawdata["daily"][day]
        return self.__dailyDict


# End of module OpenWeatherMap for OneCallApi
