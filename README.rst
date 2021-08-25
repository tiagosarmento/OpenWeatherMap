POCAR - Process One Call Api Response
=====================================

.. |Code QL Analysis| image:: https://github.com/tiagosarmento/pocar/actions/workflows/codeql-analysis.yml/badge.svg
   :target: https://github.com/tiagosarmento/pocar/actions/workflows/codeql-analysis.yml

.. |FLake8 Lint Analysis| image:: https://github.com/tiagosarmento/pocar/actions/workflows/flake8-analysis.yml/badge.svg
   :target: https://github.com/tiagosarmento/pocar/actions/workflows/flake8-analysis.yml

.. |Pytest Analysis| image:: https://github.com/tiagosarmento/pocar/actions/workflows/pytest-analysis.yml/badge.svg
   :target: https://github.com/tiagosarmento/pocar/actions/workflows/pytest-analysis.yml

.. |Code Style Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://black.readthedocs.io/en/stable/

.. |made-with-sphinx-doc| image:: https://img.shields.io/badge/Made%20with-Sphinx-1f425f.svg
   :target: https://www.sphinx-doc.org/

.. |Python Versions| image:: https://img.shields.io/pypi/pyversions/pocar

.. |License: MIT| image:: https://img.shields.io/github/license/tiagosarmento/pocar

.. |Release Date| image:: https://img.shields.io/github/release-date/tiagosarmento/pocar

.. |Release Version| image:: https://img.shields.io/github/v/release/tiagosarmento/pocar

.. |Issues Open| image:: https://img.shields.io/github/issues-raw/tiagosarmento/pocar

.. |Tag Version| image:: https://img.shields.io/github/v/tag/tiagosarmento/pocar

.. |Pypi Version| image:: https://img.shields.io/pypi/v/pocar

.. |Pypi Status| image:: https://img.shields.io/pypi/status/pocar

.. |Pypi License| image:: https://img.shields.io/pypi/l/pocar


|Code QL Analysis| |FLake8 Lint Analysis| |Pytest Analysis|

|Code Style Black| |made-with-sphinx-doc| |Python Versions| |License: MIT|

|Release Date| |Release Version| |Tag Version| |Issues Open|

|Pypi Version| |Pypi Status| |Pypi License|

----

This python package aims to process Open Weather data provided by One Call API.
The access to One Call API is free, but an account in Open Weather is required, see: [OpenWeather Account](https://openweathermap.org/full-price#current)

The One Call API provides the following weather data for any geographical coordinates:
* Current weather
* Minute forecast for 1 hour
* Hourly forecast for 48 hours
* Daily forecast for 7 days
* National weather alerts

See full documentation for One Call API: [One Call API documentation](https://openweathermap.org/api/one-call-api)

This python package processes the One Call Api response, making data available to user.

For further details refer to [wiki](https://github.com/tiagosarmento/pocar/wiki)
