#!/usr/bin/env python3

# Begin of module OpenWeatherMap for OneCallApi response

import json
import logging
import requests
import sys
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

    # Get OpenWeatherMap raw data from OneCallApi response.
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
        super().__init__(lat, lon, key)  # Init parent attributes
        self.__dt = "N/A"  # Current time, Unix, UTC
        self.__sunrise = "N/A"  # Sunrise time, Unix, UTC
        self.__sunset = "N/A"  # Sunset time, Unix, UTC
        self.__temp = "N/A"  # Temperature
        self.__tempfeel = "N/A"  # Temperature feel
        self.__pressure = "N/A"  # Atmospheric pressure on the sea level, hPa
        self.__humidity = "N/A"  # Humidity, %
        self.__dewpoint = "N/A"  # Atmospheric temperature
        self.__clouds = "N/A"  # Cloudiness, %
        self.__uvi = "N/A"  # UV index
        self.__visibility = "N/A"  # Average visibility, metres
        self.__windspeed = "N/A"  # Wind speed (m/s)
        self.__windgust = "N/A"  # Wind gust (where available)
        self.__winddeg = "N/A"  # Wind direction, degrees (meteorological)
        self.__rain1h = "N/A"  # Rain volume for last hour, mm (where available)
        self.__snow1h = "N/A"  # Snow volume for last hour, mm (where available)
        self.__weatherid = "N/A"  # Weather condition id
        self.__weathermain = (
            "N/A"
        )  # Group of weather parameters (Rain, Snow, Extreme etc.)
        self.__weatherdescription = (
            "N/A"
        )  # Weather condition within the group (full list of weather conditions).
        self.__weathericon = "N/A"  # Weather icon id. How to get icons

    # Dump OpenWeatherMap, Current Weather attributes.
    # It requires logging level INFO to be enabled.
    def dumpCurrentWeatherData(self):
        logger.info("Current date                : %s", self.__dt)
        logger.info("Current sunrise             : %s", self.__sunrise)
        logger.info("Current sunset              : %s", self.__sunset)
        logger.info("Current temperature         : %s", self.__temp)
        logger.info("Current temperature feel    : %s", self.__tempfeel)
        logger.info("Current pressure            : %s", self.__pressure)
        logger.info("Current humidity            : %s", self.__humidity)
        logger.info("Current dew point           : %s", self.__dewpoint)
        logger.info("Current clouds              : %s", self.__clouds)
        logger.info("Current uvi                 : %s", self.__uvi)
        logger.info("Current visibility          : %s", self.__visibility)
        logger.info("Current wind speed          : %s", self.__windspeed)
        logger.info("Current wind gust           : %s", self.__windgust)
        logger.info("Current wind deg            : %s", self.__winddeg)
        logger.info("Current rain 1h             : %s", self.__rain1h)
        logger.info("Current snow 1h             : %s", self.__snow1h)
        logger.info("Current weather id          : %s", self.__weatherid)
        logger.info("Current weather main        : %s", self.__weathermain)
        logger.info("Current weather description : %s", self.__weatherdescription)
        logger.info("Current weather icon        : %s", self.__weathericon)

    # Get Current time, Unix, UTC
    # metrics defaults to 0: date in human readable format
    # any other value, date is represented as UNIX seconds
    def getCurrentTime(self, metrics=0):
        self.refreshData()
        self.__dt = self._rawdata["current"]["dt"]
        if metrics == 0:
            retTime = datetime.fromtimestamp(self.__dt)
            logger.info("RET TIME: %s", retTime)
        else:
            retTime = self.__dt
        return retTime

    # Get Sunrise time, Unix, UTC
    def getCurrentSunrise(self):
        self.refreshData()
        self.__sunrise = self._rawdata["current"]["sunrise"]
        return self.__sunrise

    # Get Sunset time, Unix, UTC
    def getCurrentSunset(self):
        self.refreshData()
        self.__sunset = self._rawdata["current"]["sunset"]
        return self.__sunset

    # Get Current Temperature
    def getCurrentTemperature(self):
        self.refreshData()
        self.__temp = self._rawdata["current"]["temp"]
        return self.__temp

    # Get Current Temperature feel
    def getCurrentTemperatureFeel(self):
        self.refreshData()
        self.__tempfeel = self._rawdata["current"]["feels_like"]
        return self.__tempfeel

    # Get Current Atmospheric pressure on the sea level, hPa
    def getCurrentPressure(self):
        self.refreshData()
        self.__pressure = self._rawdata["current"]["pressure"]
        return self.__pressure

    # Get Current Humidity, %
    def getCurrentHumidity(self):
        self.refreshData()
        self.__humidity = self._rawdata["current"]["humidity"]
        return self.__humidity

    # Get Current Atmospheric temperature
    def getCurrentDewPoint(self):
        self.refreshData()
        self.__dewpoint = self._rawdata["current"]["dew_point"]
        return self.__dewpoint

    # Get Current Cloudiness, %
    def getCurrentClouds(self):
        self.refreshData()
        self.__clouds = self._rawdata["current"]["clouds"]
        return self.__clouds

    # Get Current UV index
    def getCurrentUvi(self):
        self.refreshData()
        self.__uvi = self._rawdata["current"]["uvi"]
        return self.__uvi

    # Get Current Average visibility, metres
    def getCurrentVisibility(self):
        self.refreshData()
        self.__visibility = self._rawdata["current"]["visibility"]
        return self.__visibility

    # Get Current Wind speed (m/s)
    def getCurrentWindSpeed(self):
        self.refreshData()
        self.__windspeed = self._rawdata["current"]["wind_speed"]
        return self.__windspeed

    # Get Current Wind gust (where available)
    def getCurrentWindGust(self):
        self.refreshData()
        if "wind_gust" in self._rawdata["current"]:
            self.__windgust = self._rawdata["current"]["wind_gust"]
        else:
            self.__windgust = "N/A"
        return self.__windgust

    # Get Current Wind direction, degrees (meteorological)
    def getCurrentWindDirection(self):
        self.refreshData()
        self.__winddeg = self._rawdata["current"]["wind_deg"]
        return self.__winddeg

    # Get Current Rain volume for last hour, mm (where available)
    def getCurrentRainVolume(self):
        self.refreshData()
        if "rain" in self._rawdata["current"]:
            self.__rain1h = self._rawdata["current"]["rain"]["1h"]
        else:
            self.__rain1h = "N/A"
        return self.__rain1h

    # Get Current Snow volume for last hour, mm (where available)
    def getCurrentSnowVolume(self):
        self.refreshData()
        if "snow" in self._rawdata["current"]:
            self.__snow1h = self._rawdata["current"]["snow"]["1h"]
        else:
            self.__snow1h = "N/A"
        return self.__snow1h

    # Get Current Weather condition id
    def getCurrentWeatherConditionId(self):
        self.refreshData()
        weatherDict = self._rawdata["current"]["weather"][0]
        self.__weatherid = weatherDict["id"]
        return self.__weatherid

    # Get Group of weather parameters (Rain, Snow, Extreme etc.)
    def getCurrentWeatherConditionMain(self):
        self.refreshData()
        weatherDict = self._rawdata["current"]["weather"][0]
        self.__weathermain = weatherDict["main"]
        return self.__weathermain

    # Get Weather condition within the group (full list of weather conditions)
    def getCurrentWeatherConditionDescription(self):
        self.refreshData()
        weatherDict = self._rawdata["current"]["weather"][0]
        self.__weatherdescription = weatherDict["description"]
        return self.__weatherdescription

    # Get Weather icon id. How to get icons
    def getCurrentWeatherConditionIconId(self):
        self.refreshData()
        weatherDict = self._rawdata["current"]["weather"][0]
        self.__weathericon = weatherDict["icon"]
        return self.__weathericon


# Derived Class to handle Minutely weather data API response
# Minutely holds the precipitation forecast for the next hour in a minutely basis
class OneCallApiMinutely(OneCallApi):
    def __init__(self, lat, lon, key):
        super().__init__(lat, lon, key)  # Init parent attributes
        self.__minutPrecDict = dict()

    # Gets 61 values: current + next 60 minutes
    def getMinutelyData(self, minute=0):
        self.refreshData()
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
        self.refreshData()
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
        self.refreshData()
        self.__dailyDict = self._rawdata["daily"][day]
        return self.__dailyDict


# End of module OpenWeatherMap for OneCallApi
