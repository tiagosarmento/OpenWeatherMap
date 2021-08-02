#!/usr/bin/env python3

# Begin of module Open Weather Map for One Call API

import time
import sys
import requests
import logging
from datetime import datetime

# Uncomment this line to suppress warning message due to:
#    InsecureRequestWarning: Unverified HTTPS request is being made.
#    Adding certificate verification is strongly advised.
#    See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
# We get this warning because an HTTP GET request is made with SSL verification disabled
requests.packages.urllib3.disable_warnings()

# Set local logger to the root logger, to inherit root settings
logger = logging.getLogger(__name__)


# Base Class to handle One Call API from Open Weather Map
class OneCallApi:
    def __init__(self, lat, lon, key, timeThrs=60):
        self._lat      = lat
        self._lon      = lon
        self._key      = key
        self._timeThrs = timeThrs
        self._ocadata  = dict()
        self._dataTime = 0
        self._url      = f("https://api.openweathermap.org/data/2.5/onecall?lat={self._lat}&lon={self._lon}"
                           "&units=metric&appid={self._key}")

    # Dump Base Class attributes, these are the base configuration to access Open Weather Map for One Call API.
    # It requires logging level INFO to be enabled.
    def dumpConfig(self):
        logger.info("Configured latitude       : %s", self._lat)
        logger.info("Configured longitude      : %s", self._lon)
        logger.info("Configured OWM API key    : %s", self._key)
        logger.info("Configured OWM OCA Url    : %s", self._url)
        logger.info("Configured Time Threshold : %s", self._timeThrs)

    # Verify data validity
    # To void too many calls to Open Weather Map, a threshold is set to consider if data is still valid before
    # pulling new data
    def __isDataValid(self):
        if len(self._ocadata) == 0:
            # If dictionary is empty, no data to verify
            logger.debug("One Call API response data is empty")
            return False
        elif self._timeThrs < (time.time() - self._dataTime):
            # If time threshold exceed, current data is considered outdated
            logger.debug("One Call API response data is outdated")
            return False
        else:
            logger.debug("One Call API response data is valid")
            return True

    # Get Open Weather Map data from One Call API
    # Data is stored as a dictionary in this class
    def __getData(self):
        req = requests.get(self._url, verify=False)
        try:
            req.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            logger.exception("HTTP Error: %s", errh)
            sys.exit(1)
        except requests.exceptions.ConnectionError as errc:
            logger.exception("Connection Error: %s", errc)
            sys.exit(1)
        except requests.exceptions.TimeoutError as errt:
            logger.exception("Timeout Error: %s", errt)
            sys.exit(1)
        except requests.exceptions.RequestsException as err:
            logger.exception("Requests Error: %s", err)
            sys.exit(1)
        else:
            self._ocadata  = req.json()
            self._dataTime = time.time()

    # Make an update of Open Weather Map data
    def refreshData(self):
        if self.__isDataValid() is False:
            self.__getData()
            logger.debug("Data was updated")
        else:
            logger.debug("Data is stil valid")

    # Get geographical coordinates of the location (latitude)
    def getLat(self):
        return self._lat

    # Get geographical coordinates of the location (longitude)
    def getLon(self):
        return self._lon

    # Get Open Weather Map API Key
    def getKey(self):
        return self._key

    # Get Open Weather Map URL for One Call API HTTP GET call
    def getUrl(self):
        return self._url

    # Get Timezone name for the requested location
    def getTimezone(self):
        self.refreshData()
        return self._ocadata["timezone"]

    # Get Timezone offset Shift in seconds from UTC
    def getTimezoneOffset(self):
        self.refreshData()
        return self._ocadata["timezone_offset"]


# Derived Class to handle Current weather data API response
class OneCallApiCurrent(OneCallApi):
    def __init__(self, lat, lon, key, timeThrs=60):
        super().__init__(lat, lon, key, timeThrs) # Init parent attributes
        self.__dt                  = "N/A" # Current time, Unix, UTC
        self.__sunrise             = "N/A" # Sunrise time, Unix, UTC
        self.__sunset              = "N/A" # Sunset time, Unix, UTC
        self.__temp                = "N/A" # Temperature
        self.__tempfeel            = "N/A" # Temperature feel
        self.__pressure            = "N/A" # Atmospheric pressure on the sea level, hPa
        self.__humidity            = "N/A" # Humidity, %
        self.__dewpoint            = "N/A" # Atmospheric temperature
        self.__clouds              = "N/A" # Cloudiness, %
        self.__uvi                 = "N/A" # UV index
        self.__visibility          = "N/A" # Average visibility, metres
        self.__windspeed           = "N/A" # Wind speed (m/s)
        self.__windgust            = "N/A" # Wind gust (where available)
        self.__winddeg             = "N/A" # Wind direction, degrees (meteorological)
        self.__rain1h              = "N/A" # Rain volume for last hour, mm (where available)
        self.__snow1h              = "N/A" # Snow volume for last hour, mm (where available)
        self.__weatherid           = "N/A" # Weather condition id
        self.__weathermain         = "N/A" # Group of weather parameters (Rain, Snow, Extreme etc.)
        self.__weatherdescription  = "N/A" # Weather condition within the group (full list of weather conditions).
        self.__weathericon         = "N/A" # Weather icon id. How to get icons

    # Dump Open Weather Map, Current Weather attributes.
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
        self.__dt = self._ocadata["current"]["dt"]
        if metrics == 0:
            retTime = datetime.fromtimestamp(self.__dt)
            logger.info("RET TIME: %s", retTime)
        else:
            retTime = self.__dt
        return retTime

    # Get Sunrise time, Unix, UTC
    def getCurrentSunrise(self):
        self.refreshData()
        self.__sunrise = self._ocadata["current"]["sunrise"]
        return self.__sunrise

    # Get Sunset time, Unix, UTC
    def getCurrentSunset(self):
        self.refreshData()
        self.__sunset = self._ocadata["current"]["sunset"]
        return self.__sunset

    # Get Current Temperature
    def getCurrentTemperature(self):
        self.refreshData()
        self.__temp = self._ocadata["current"]["temp"]
        return self.__temp

    # Get Current Temperature feel
    def getCurrentTemperatureFeel(self):
        self.refreshData()
        self.__tempfeel = self._ocadata["current"]["feels_like"]
        return self.__tempfeel

    # Get Current Atmospheric pressure on the sea level, hPa
    def getCurrentPressure(self):
        self.refreshData()
        self.__pressure = self._ocadata["current"]["pressure"]
        return self.__pressure

    # Get Current Humidity, %
    def getCurrentHumidity(self):
        self.refreshData()
        self.__humidity = self._ocadata["current"]["humidity"]
        return self.__humidity

    # Get Current Atmospheric temperature
    def getCurrentDewPoint(self):
        self.refreshData()
        self.__dewpoint = self._ocadata["current"]["dew_point"]
        return self.__dewpoint

    # Get Current Cloudiness, %
    def getCurrentClouds(self):
        self.refreshData()
        self.__clouds = self._ocadata["current"]["clouds"]
        return self.__clouds

    # Get Current UV index
    def getCurrentUvi(self):
        self.refreshData()
        self.__uvi = self._ocadata["current"]["uvi"]
        return self.__uvi

    # Get Current Average visibility, metres
    def getCurrentVisibility(self):
        self.refreshData()
        self.__visibility = self._ocadata["current"]["visibility"]
        return self.__visibility

    # Get Current Wind speed (m/s)
    def getCurrentWindSpeed(self):
        self.refreshData()
        self.__windspeed = self._ocadata["current"]["wind_speed"]
        return self.__windspeed

    # Get Current Wind gust (where available)
    def getCurrentWindGust(self):
        self.refreshData()
        if "wind_gust" in self._ocadata["current"]:
            self.__windgust = self._ocadata["current"]["wind_gust"]
        else:
            self.__windgust = "N/A"
        return self.__windgust

    # Get Current Wind direction, degrees (meteorological)
    def getCurrentWindDirection(self):
        self.refreshData()
        self.__winddeg = self._ocadata["current"]["wind_deg"]
        return self.__winddeg

    # Get Current Rain volume for last hour, mm (where available)
    def getCurrentRainVolume(self):
        self.refreshData()
        if "rain" in self._ocadata["current"]:
            self.__rain1h = self._ocadata["current"]["rain"]["1h"]
        else:
            self.__rain1h = "N/A"
        return self.__rain1h

    # Get Current Snow volume for last hour, mm (where available)
    def getCurrentSnowVolume(self):
        self.refreshData()
        if "snow" in self._ocadata["current"]:
            self.__snow1h = self._ocadata["current"]["snow"]["1h"]
        else:
            self.__snow1h = "N/A"
        return self.__snow1h

    # Get Current Weather condition id
    def getCurrentWeatherConditionId(self):
        self.refreshData()
        weatherDict = self._ocadata["current"]["weather"][0]
        self.__weatherid = weatherDict["id"]
        return self.__weatherid

    # Get Group of weather parameters (Rain, Snow, Extreme etc.)
    def getCurrentWeatherConditionMain(self):
        self.refreshData()
        weatherDict = self._ocadata["current"]["weather"][0]
        self.__weathermain = weatherDict["main"]
        return self.__weathermain

    # Get Weather condition within the group (full list of weather conditions)
    def getCurrentWeatherConditionDescription(self):
        self.refreshData()
        weatherDict = self._ocadata["current"]["weather"][0]
        self.__weatherdescription = weatherDict["description"]
        return self.__weatherdescription

    # Get Weather icon id. How to get icons
    def getCurrentWeatherConditionIconId(self):
        self.refreshData()
        weatherDict = self._ocadata["current"]["weather"][0]
        self.__weathericon = weatherDict["icon"]
        return self.__weathericon


# Derived Class to handle Minutely weather data API response
# Minutely holds the precipitation forecast for the next hour in a minutely basis
class OneCallApiMinutely(OneCallApi):
    def __init__(self, lat, lon, key, timeThrs=60):
        super().__init__(lat, lon, key, timeThrs) # Init parent attributes
        self.__minutPrecDict = dict()

    # Gets 61 values: current + next 60 minutes
    def getMinutelyData(self, minute=0):
        self.refreshData()
        if minute == 0:
            # gets the full dictionary data
            self.__minutPrecDict = self._ocadata["minutely"]
        else:
            # gets current time + minute precipitation forecast
            self.__minutPrecDict = self._ocadata["minutely"][minute]["precipitation"]
        return self.__minutPrecDict


# Derived Class to handle Hourly weather data API response
# Hourly holds the weather forecast for the next 48 hours in a hourly basis
class OneCallApiHourly(OneCallApi):
    def __init__(self, lat, lon, key, timeThrs=60):
        super().__init__(lat, lon, key, timeThrs) # Init parent attributes
        self.__hourlyDict = dict()

    # Gets 48 values: weather for next 48 hours
    def getHourlyData(self, hour=0):
        self.refreshData()
        self.__hourlyDict = self._ocadata["hourly"][hour]
        return self.__hourlyDict


# Derived Class to handle Daily weather data API response
# Daily holds the weather forecast for the next 7 days in a daily basis
class OneCallApiDaily(OneCallApi):
    def __init__(self, lat, lon, key, timeThrs=60):
        super().__init__(lat, lon, key, timeThrs) # Init parent attributes
        self.__dailyDict = dict()

    # Gets 7 values: weather today + for next 7 days
    def getDailyData(self, day=0):
        self.refreshData()
        self.__dailyDict = self._ocadata["daily"][day]
        return self.__dailyDict

# End of module Open Weather Map for One Call API
