"""This module provides a base class to handle One Call Api response from OpenWeatherMap."""
import json
import logging
import time

import requests

# Uncomment this line to suppress warning message due to:
#    InsecureRequestWarning: Unverified HTTPS request is being made.
#    Adding certificate verification is strongly advised.
#    See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
# We get this warning because an HTTP GET request is made with SSL verification disabled
requests.packages.urllib3.disable_warnings()

# Set local logger to the root logger, to inherit root settings
logger = logging.getLogger(__name__)


class OneCallApi:
    """
    Base Class to handle OneCallApi response from OpenWeatherMap.

    :param lat: Geographical coordinates of the location (latitude)
    :type lat: float, range [-90; 90]

    :param lon: Geographical coordinates of the location (longitude)
    :type lon: float, range [-180; 180]

    :param key: The OpenWeatherMap One Call Api key value
    :type key: hex, 128-bit hash key

    :param exc: The excluded fields in One Call Api response
    :type exc: comma separated str, optional, values ["current", "minutely", "hourly", "daily", "alerts"]

    :ivar _rawdata: The raw data of One Call Api response

    :ivar _timestamp: Timestamp of when One Call Api call response was received

    :ivar __url: The URL used to perform the One Call Api call
    """

    def __init__(self, lat, lon, key, exc=""):
        """This is the constructor method."""
        self.lat = lat
        self.lon = lon
        self.key = key
        self.exc = exc
        self._rawdata = {}
        self._timestamp = 0
        self.__url = (
            f"https://api.openweathermap.org/data/2.5/onecall?lat={self._lat}&lon={self._lon}"
            f"&exclude={self._exc}&units=metric&appid={self._key}"
        )

    @property
    def lat(self):
        """The getter/setter for attribute :attr:`lat`."""
        logger.debug("Get method for 'lat' attribute")
        return self._lat

    @lat.setter
    def lat(self, lat):
        logger.debug("Set method for 'lat' attribute")
        if lat < -90.0 or lat > 90.0:
            raise ValueError("The 'lat' argument must be within range [-90, 90]")
        self._lat = lat
        logger.debug("Set 'lat' value to: %s", self._lat)

    @property
    def lon(self):
        """The getter/setter for attribute :attr:`lon`."""
        logger.debug("Get method for 'lon' attribute")
        return self._lon

    @lon.setter
    def lon(self, lon):
        logger.debug("Set method for 'lon' attribute")
        if lon < -180.0 or lon > 180.0:
            raise ValueError("The 'lon' argument must be within range [-180, 180]")
        self._lon = lon
        logger.debug("Set 'lon' value to: %s", self._lon)

    @property
    def key(self):
        """The getter/setter for attribute :attr:`key`."""
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
        self._key = key
        logger.debug("Set 'key' value to: %s", self._key)

    @property
    def exc(self):
        """The getter/setter for attribute :attr:`exc`."""
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
            spec_word_list = ["current", "minutely", "hourly", "daily", "alerts"]
            exc_word_list = exc.split(",")
            for exc_word in exc_word_list:
                if exc_word in spec_word_list:
                    logger.debug("The 'exc' argument contains word: %s", exc_word)
                else:
                    logger.error("The 'exc' argument contains an invalid word: %s", exc_word)
                    raise ValueError(
                        "The 'exc' argument must specific words: (current, minutely, hourly, daily, alerts)"
                    )
            self._exc = exc
        logger.debug("Set 'exc' value to: %s", self._exc)

    def config(self):
        """
        | The config method.

        | Returns a dictionary containg the configuration used to call OpenWeatherMap for One Call Api.
        | The dictionary is in form of (key, value), as follows:
        | [ ( lat , :attr:`~pocar.OneCallAPi.OneCallAPi.lat` ),
        |   ( lon , :attr:`~pocar.OneCallAPi.OneCallAPi.lon` ),
        |   ( key , :attr:`~pocar.OneCallAPi.OneCallAPi.key` ),
        |   ( url , :attr:`~pocar.OneCallAPi.OneCallAPi.__url` )]

        :return: Configuration to call OpenWeatherMap for One Call Api
        :rtype: dict
        """
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

    def raw_data(self):
        """
        | The raw_data method.

        | Returns the variable :attr:`~pocar.OneCallAPi.OneCallAPi._raw_data`.
        | This variable contains the One Call Api response raw data as a dictionary

        :return: raw data as a dictionary
        :rtype: dict
        """
        return self._rawdata

    def __get_data(self):
        """
        | The __get_data method.

        | This method makes an HTTP request to OpenWeatherMap.
        | The URL for the call is :attr:`~pocar.OneCallAPi.OneCallAPi.__url`
        | The retrieved data is stored in :attr:`~pocar.OneCallAPi.OneCallAPi._rawdata`

        :return: `True` if data successfully retrieved, `False` otherwise
        :rtype: bool
        """
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

    def update_data(self):
        """
        | The update_data method.

        This method triggers a call to :meth:`~pocar.OneCallAPi.OneCallAPi.__get_data`.

        :return: `True` if data successfully update, `False` otherwise
        :rtype: bool
        """
        return self.__get_data()

    def timezone(self):
        """
        | The timezone method.

        | Returns the value for timezone from One Call Api response.
        | One Call Api response field is: `["timezone"]`

        :return: Timezone name for the requested location
        :rtype: str
        """
        value = ""
        if "timezone" in self._rawdata:
            value = self._rawdata["timezone"]
        return value

    def timezone_offset(self):
        """
        | The timezone_offset method.

        | Returns the value for timezone offset from One Call Api response.
        | One Call Api response field is: `["timezone_offset"]`

        :return: Shift in seconds from UTC
        :rtype: int
        """
        value = 0
        if "timezone_offset" in self._rawdata:
            value = self._rawdata["timezone_offset"]
        return value

    def timestamp(self):
        """
        | The timestamp method.

        | Returns the value of :attr:`~pocar.OneCallAPi.OneCallAPi._timestamp`,
        | that holds the timestamp of when One Call Api call response was received.


        :return: unix seconds value
        :rtype: float
        """
        return self._timestamp
