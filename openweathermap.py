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
            logger.error("The 'key' argument must be an hash value of 32 hexadecimal digits")
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
            raise ValueError("The 'exc' argument must be a comma-delimited string (without spaces)")
        else:
            # the exclusion shall contain specific words
            specWordList = ["current", "minutely", "hourly", "daily", "alerts"]
            excWordList = exc.split(",")
            for excWord in excWordList:
                if excWord in specWordList:
                    logger.debug("The 'exc' argument contains word: %s", excWord)
                else:
                    logger.error("The 'exc' argument contains an invalid word: %s", excWord)
                    raise ValueError("The 'exc' argument must specific words: (current, minutely, hourly, daily, alerts)")
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
        super().__init__(lat, lon, key, "minutely,daily,hourly,alerts")

    def __is_data_available(self, field):
        value = False
        if ("current" in self._rawdata) and (field in self._rawdata["current"]):
            value = True
        return value

    def __extract_date_field(self, field, metrics=0):
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
# Gets 61 values: current + next 60 minutes
class OneCallApiMinutely(OneCallApi):
    def __init__(self, lat, lon, key):
        super().__init__(lat, lon, key, "current,daily,hourly,alerts")

    def __is_data_available(self, minute, field):
        value = False
        if ("minutely" in self._rawdata) and (field in self._rawdata["minutely"][minute]):
            value = True
        return value

    def __extract_date_field(self, minute, field, metrics=0):
        value = "N/A"
        if self.__is_data_available(minute, field) is True:
            if metrics == 0:
                dt = datetime.fromtimestamp(self._rawdata["minutely"][minute][field])
                value = f"{dt:%Y-%m-%d %H:%M:%S}"
            else:
                value = self._rawdata["minutely"][minute][field]
        logger.debug("Value for %s is: %s", field, value)
        return value

    def __extract_value_field(self, minute, field):
        value = "N/A"
        if self.__is_data_available(minute, field) is True:
            value = self._rawdata["minutely"][minute][field]
        logger.debug("Value for %s is: %s", field, value)
        return value

    def raw_data_minutely(self):
        value = dict()
        if "minutely" in self._rawdata:
            value = self._rawdata["minutely"]
        return value

    def precipitation(self, minute=0, all_values=False):
        if minute < 0 or minute > 60:
            raise ValueError("The 'minute' argument must be within range [0, 60]")
        elif all_values is True:
            value = [0] * 61  # Initialize the 61 precipitation values
            for idx in range(61):
                value[idx] = self.__extract_value_field(idx, "precipitation")
        else:
            value = self.__extract_value_field(minute, "precipitation")
        return value

    def data_time(self, minute=0, metrics=0, all_values=False):
        if minute < 0 or minute > 60:
            raise ValueError("The 'minute' argument must be within range [0, 60]")
        elif all_values is True:
            value = [0] * 61  # Initialize the 61 data time values
            for idx in range(61):
                value[idx] = self.__extract_date_field(idx, "dt", metrics)
        else:
            value = self.__extract_date_field(minute, "dt", metrics)
        return value


# Derived Class to handle Hourly weather data API response
# Hourly holds the weather forecast for the next 48 hours in a hourly basis
# Values are for current hour + 47
class OneCallApiHourly(OneCallApi):
    def __init__(self, lat, lon, key):
        super().__init__(lat, lon, key, "current,daily,minutely,alerts")

    def __is_data_available(self, hour, field):
        value = False
        if ("hourly" in self._rawdata) and (field in self._rawdata["hourly"][hour]):
            value = True
        return value

    def __extract_date_field(self, hour, field, metrics=0):
        value = "N/A"
        if self.__is_data_available(hour, field) is True:
            if metrics == 0:
                dt = datetime.fromtimestamp(self._rawdata["hourly"][hour][field])
                value = f"{dt:%Y-%m-%d %H:%M:%S}"
            else:
                value = self._rawdata["hourly"][hour][field]
        logger.debug("Value for %s is: %s", field, value)
        return value

    def __extract_value_field(self, hour, field):
        value = "N/A"
        if self.__is_data_available(hour, field) is True:
            value = self._rawdata["hourly"][hour][field]
        logger.debug("Value for %s is: %s", field, value)
        return value

    def __extract_value_set(self, hour, field, all_values):
        if hour < 0 or hour > 48:
            raise ValueError("The 'hour' argument must be within range [0, 48]")
        elif all_values is True:
            value = [0] * 48  # Initialize the 48 data time values
            for idx in range(48):
                value[idx] = self.__extract_value_field(idx, field)
        else:
            value = self.__extract_value_field(hour, field)
        return value

    def __extract_weather_field(self, hour, field):
        value = "N/A"
        if ("hourly" in self._rawdata) and ("weather" in self._rawdata["hourly"][hour]):
            if field in self._rawdata["hourly"][hour]["weather"][0]:
                value = self._rawdata["hourly"][hour]["weather"][0][field]
        logger.debug("Value for %s is: %s", field, value)
        return value

    def __extract_weather_set(self, hour, field, all_values):
        if hour < 0 or hour > 48:
            raise ValueError("The 'hour' argument must be within range [0, 48]")
        elif all_values is True:
            value = [0] * 48  # Initialize the 48 data time values
            for idx in range(48):
                value[idx] = self.__extract_weather_field(idx, field)
        else:
            value = self.__extract_weather_field(hour, field)
        return value

    def raw_data_hourly(self):
        value = dict()
        if "hourly" in self._rawdata:
            value = self._rawdata["hourly"]
        return value

    def data_time(self, hour=0, metrics=0, all_values=False):
        if hour < 0 or hour > 48:
            raise ValueError("The 'hour' argument must be within range [0, 48]")
        elif all_values is True:
            value = [0] * 48  # Initialize the 48 data time values
            for idx in range(48):
                value[idx] = self.__extract_date_field(idx, "dt", metrics)
        else:
            value = self.__extract_date_field(hour, "dt", metrics)
        return value

    def temp(self, hour=0, all_values=False):
        return self.__extract_value_set(hour, "temp", all_values)

    def feels_like(self, hour=0, all_values=False):
        return self.__extract_value_set(hour, "feels_like", all_values)

    def pressure(self, hour=0, all_values=False):
        return self.__extract_value_set(hour, "pressure", all_values)

    def humidity(self, hour=0, all_values=False):
        return self.__extract_value_set(hour, "humidity", all_values)

    def dew_point(self, hour=0, all_values=False):
        return self.__extract_value_set(hour, "dew_point", all_values)

    def uvi(self, hour=0, all_values=False):
        return self.__extract_value_set(hour, "uvi", all_values)

    def clouds(self, hour=0, all_values=False):
        return self.__extract_value_set(hour, "clouds", all_values)

    def visibility(self, hour=0, all_values=False):
        return self.__extract_value_set(hour, "visibility", all_values)

    def wind_speed(self, hour=0, all_values=False):
        return self.__extract_value_set(hour, "wind_speed", all_values)

    def wind_deg(self, hour=0, all_values=False):
        return self.__extract_value_set(hour, "wind_deg", all_values)

    def wind_gust(self, hour=0, all_values=False):
        return self.__extract_value_set(hour, "wind_gust", all_values)

    def weather_id(self, hour=0, all_values=False):
        return self.__extract_weather_set(hour, "id", all_values)

    def weather_main(self, hour=0, all_values=False):
        return self.__extract_weather_set(hour, "main", all_values)

    def weather_description(self, hour=0, all_values=False):
        return self.__extract_weather_set(hour, "description", all_values)

    def weather_icon(self, hour=0, all_values=False):
        return self.__extract_weather_set(hour, "icon", all_values)

    def pop(self, hour=0, all_values=False):
        return self.__extract_value_set(hour, "pop", all_values)


# Derived Class to handle Daily weather data API response
# Daily holds the weather forecast for the next 7 days in a daily basis
# Gets 7 values: weather today + for next 7 days
class OneCallApiDaily(OneCallApi):
    def __init__(self, lat, lon, key):
        super().__init__(lat, lon, key, "current,hourly,minutely,alerts")

    def __is_data_available(self, day, field):
        value = False
        if ("daily" in self._rawdata) and (field in self._rawdata["daily"][day]):
            value = True
        return value

    def __extract_date_field(self, day, field, metrics=0):
        value = "N/A"
        if self.__is_data_available(day, field) is True:
            if metrics == 0:
                dt = datetime.fromtimestamp(self._rawdata["daily"][day][field])
                value = f"{dt:%Y-%m-%d %H:%M:%S}"
            else:
                value = self._rawdata["daily"][day][field]
        logger.debug("Value for %s is: %s", field, value)
        return value

    def __extract_date_set(self, day, field, metrics=0, all_values=False):
        if day < 0 or day > 7:
            raise ValueError("The 'day' argument must be within range [0, 7]")
        elif all_values is True:
            value = [0] * 7  # Initialize the 48 data time values
            for idx in range(7):
                value[idx] = self.__extract_date_field(idx, field, metrics)
        else:
            value = self.__extract_date_field(day, field, metrics)
        return value

    def __extract_temp_field(self, day, group, field):
        value = "N/A"
        if self.__is_data_available(day, group) is True:
            if field in self._rawdata["daily"][day][group]:
                value = self._rawdata["daily"][day][group][field]
        logger.debug("Value for %s is: %s", field, value)
        return value

    def __extract_temp_set(self, day, group, field, all_values):
        if day < 0 or day > 7:
            raise ValueError("The 'day' argument must be within range [0, 7]")
        elif all_values is True:
            value = [0] * 7  # Initialize the 7 data time values
            for idx in range(7):
                value[idx] = self.__extract_temp_field(idx, group, field)
        else:
            value = self.__extract_temp_field(day, group, field)
        return value

    def __extract_value_field(self, day, field):
        value = "N/A"
        if self.__is_data_available(day, field) is True:
            value = self._rawdata["daily"][day][field]
        logger.debug("Value for %s is: %s", field, value)
        return value

    def __extract_value_set(self, day, field, all_values):
        if day < 0 or day > 7:
            raise ValueError("The 'day' argument must be within range [0, 7]")
        elif all_values is True:
            value = [0] * 7  # Initialize the 7 data time values
            for idx in range(7):
                value[idx] = self.__extract_value_field(idx, field)
        else:
            value = self.__extract_value_field(day, field)
        return value

    def __extract_weather_field(self, day, field):
        value = "N/A"
        if ("daily" in self._rawdata) and ("weather" in self._rawdata["daily"][day]):
            if field in self._rawdata["daily"][day]["weather"][0]:
                value = self._rawdata["daily"][day]["weather"][0][field]
        logger.debug("Value for %s is: %s", field, value)
        return value

    def __extract_weather_set(self, day, field, all_values):
        if day < 0 or day > 7:
            raise ValueError("The 'hour' argument must be within range [0, 7]")
        elif all_values is True:
            value = [0] * 7  # Initialize the 7 data time values
            for idx in range(7):
                value[idx] = self.__extract_weather_field(idx, field)
        else:
            value = self.__extract_weather_field(day, field)
        return value

    def raw_data_daily(self):
        value = dict()
        if "daily" in self._rawdata:
            value = self._rawdata["daily"]
        return value

    def data_time(self, day=0, metrics=0, all_values=False):
        return self.__extract_date_set(day, "dt", metrics, all_values)

    def sunrise(self, day=0, metrics=0, all_values=False):
        return self.__extract_date_set(day, "sunrise", metrics, all_values)

    def sunset(self, day=0, metrics=0, all_values=False):
        return self.__extract_date_set(day, "sunset", metrics, all_values)

    def moonrise(self, day=0, metrics=0, all_values=False):
        return self.__extract_date_set(day, "moonrise", metrics, all_values)

    def moonset(self, day=0, metrics=0, all_values=False):
        return self.__extract_date_set(day, "moonset", metrics, all_values)

    def temp_day(self, day=0, all_values=False):
        return self.__extract_temp_set(day, "temp", "day", all_values)

    def temp_min(self, day=0, all_values=False):
        return self.__extract_temp_set(day, "temp", "min", all_values)

    def temp_max(self, day=0, all_values=False):
        return self.__extract_temp_set(day, "temp", "max", all_values)

    def temp_night(self, day=0, all_values=False):
        return self.__extract_temp_set(day, "temp", "night", all_values)

    def temp_eve(self, day=0, all_values=False):
        return self.__extract_temp_set(day, "temp", "eve", all_values)

    def temp_morn(self, day=0, all_values=False):
        return self.__extract_temp_set(day, "temp", "morn", all_values)

    def feels_like_day(self, day=0, all_values=False):
        return self.__extract_temp_set(day, "feels_like", "day", all_values)

    def feels_like_night(self, day=0, all_values=False):
        return self.__extract_temp_set(day, "feels_like", "night", all_values)

    def feels_like_eve(self, day=0, all_values=False):
        return self.__extract_temp_set(day, "feels_like", "eve", all_values)

    def feels_like_morn(self, day=0, all_values=False):
        return self.__extract_temp_set(day, "feels_like", "morn", all_values)

    def pressure(self, day=0, all_values=False):
        return self.__extract_value_set(day, "pressure", all_values)

    def humidity(self, day=0, all_values=False):
        return self.__extract_value_set(day, "humidity", all_values)

    def dew_point(self, day=0, all_values=False):
        return self.__extract_value_set(day, "dew_point", all_values)

    def wind_speed(self, day=0, all_values=False):
        return self.__extract_value_set(day, "wind_speed", all_values)

    def wind_deg(self, day=0, all_values=False):
        return self.__extract_value_set(day, "wind_deg", all_values)

    def wind_gust(self, day=0, all_values=False):
        return self.__extract_value_set(day, "wind_gust", all_values)

    def clouds(self, day=0, all_values=False):
        return self.__extract_value_set(day, "clouds", all_values)

    def pop(self, day=0, all_values=False):
        return self.__extract_value_set(day, "pop", all_values)

    def uvi(self, day=0, all_values=False):
        return self.__extract_value_set(day, "uvi", all_values)

    def weather_id(self, day=0, all_values=False):
        return self.__extract_weather_set(day, "id", all_values)

    def weather_main(self, day=0, all_values=False):
        return self.__extract_weather_set(day, "main", all_values)

    def weather_description(self, day=0, all_values=False):
        return self.__extract_weather_set(day, "description", all_values)

    def weather_icon(self, day=0, all_values=False):
        return self.__extract_weather_set(day, "icon", all_values)


# Derived Class to handle alerts data API response
class OneCallApiAlerts(OneCallApi):
    def __init__(self, lat, lon, key):
        super().__init__(lat, lon, key, "current,hourly,minutely,daily")

    def __is_data_available(self, field):
        value = False
        if ("alerts" in self._rawdata) and (field in self._rawdata["alerts"][0]):
            value = True
        return value

    def __extract_value_field(self, field):
        value = "N/A"
        if self.__is_data_available(field) is True:
            value = self._rawdata["alerts"][0][field]
        logger.debug("Value for %s is: %s", field, value)
        return value

    def __extract_date_field(self, field, metrics=0):
        value = "N/A"
        if self.__is_data_available(field) is True:
            if metrics == 0:
                dt = datetime.fromtimestamp(self._rawdata["alerts"][0][field])
                value = f"{dt:%Y-%m-%d %H:%M:%S}"
            else:
                value = self._rawdata["alerts"][0][field]
        logger.debug("Value for %s is: %s", field, value)
        return value

    def raw_data_alerts(self):
        value = dict()
        if "alerts" in self._rawdata:
            value = self._rawdata["alerts"]
        return value

    def sender_name(self):
        return self.__extract_value_field("sender_name")

    def event(self):
        return self.__extract_value_field("event")

    def start_dt(self, metrics=0):
        return self.__extract_date_field("start", metrics)

    def end_dt(self, metrics=0):
        return self.__extract_date_field("end", metrics)

    def description(self):
        return self.__extract_value_field("description")

    def tags(self):
        return self.__extract_value_field("tags")


# End of module OpenWeatherMap for OneCallApi
