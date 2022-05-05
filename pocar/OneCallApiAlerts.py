"""This module provides a class to handle One Call Api response for Alerts from OpenWeatherMap."""
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


# Derived Class to handle alerts data API response
class OneCallApiAlerts(OneCallApi):
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
        super().__init__(lat, lon, key, "current,hourly,minutely,daily")

    def __is_data_available(self, field):
        """TBD."""
        value = False
        if ("alerts" in self._rawdata) and (field in self._rawdata["alerts"][0]):
            value = True
        return value

    def __extract_value_field(self, field):
        """TBD."""
        value = "N/A"
        if self.__is_data_available(field) is True:
            value = self._rawdata["alerts"][0][field]
        logger.debug("Value for %s is: %s", field, value)
        return value

    def __extract_date_field(self, field, metrics=0):
        """TBD."""
        value = "N/A"
        if self.__is_data_available(field) is True:
            if metrics == 0:
                alert_dt = datetime.fromtimestamp(self._rawdata["alerts"][0][field])
                value = f"{alert_dt:%Y-%m-%d %H:%M:%S}"
            else:
                value = self._rawdata["alerts"][0][field]
        logger.debug("Value for %s is: %s", field, value)
        return value

    def raw_data_alerts(self):
        """
        | The raw_data_alerts metod.

        | Returns field alerts of the variable :attr:`~pocar.OneCallAPi.OneCallAPi._raw_data`
        | This variable contains the One Call Api response for alerts raw data as a dictionary

        :return: raw data as a dictionary
        :rtype: dict
        """
        value = {}
        if "alerts" in self._rawdata:
            value = self._rawdata["alerts"]
        return value

    def sender_name(self):
        """
        | The sender_name metod.

        | Returns the value for sender_name from One Call Api response
        | One Call Api response field is: `alerts.sender_name`

        :return: Name of the alert source
        :rtype: str
        """
        return self.__extract_value_field("sender_name")

    def event(self):
        """
        | The event metod.

        | Returns the value for event from One Call Api response
        | One Call Api response field is: `alerts.event`

        :return: Alert event name
        :rtype: str
        """
        return self.__extract_value_field("event")

    def start_dt(self, metrics=0):
        """
        | The start_dt metod.

        | Returns the value for start date from One Call Api response
        | This is the Date and time of the start of the alert
        | One Call Api response field is: `alerts.start`

        :param metrics: option to select metrics type, 0 = DATE string, UNIX UTC otherwise
        :type metrics: int, optional

        :return: Date and time of the end of the alert
        :rtype: date if metrics is 0 or int otherwise
        """
        return self.__extract_date_field("start", metrics)

    def end_dt(self, metrics=0):
        """
        | The end_dt metod.

        | Returns the value for end date from One Call Api response
        | This is the Date and time of the end of the alert
        | One Call Api response field is: `alerts.end`

        :param metrics: option to select metrics type, 0 = DATE string, UNIX UTC otherwise
        :type metrics: int, optional

        :return: Date and time of the end of the alert
        :rtype: date if metrics is 0 or int otherwise
        """
        return self.__extract_date_field("end", metrics)

    def description(self):
        """
        | The description metod.

        | Returns the value for description from One Call Api response
        | One Call Api response field is: `alerts.description`

        :return: Description of the alert
        :rtype: str
        """
        return self.__extract_value_field("description")

    def tags(self):
        """
        | The tags metod.

        | Returns the value for tags from One Call Api response
        | One Call Api response field is: `alerts.tags`

        :return: Type of severe weather
        :rtype: str
        """
        return self.__extract_value_field("tags")
