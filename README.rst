POCAR - Process One Call Api Response
=====================================

.. |Code QL Analysis| image:: https://github.com/tiagosarmento/pocar/actions/workflows/codeql-analysis.yml/badge.svg
   :target: https://github.com/tiagosarmento/pocar/actions/workflows/continuous_integration.yml

.. |FLake8 Lint Analysis| image:: https://github.com/tiagosarmento/pocar/actions/workflows/flake8-analysis.yml/badge.svg
   :target: https://github.com/tiagosarmento/pocar/actions/workflows/continuous_integration.yml

.. |Pytest Analysis| image:: https://github.com/tiagosarmento/pocar/actions/workflows/pytest-analysis.yml/badge.svg
   :target: https://github.com/tiagosarmento/pocar/actions/workflows/continuous_integration.yml

.. |Code Style Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://black.readthedocs.io/en/stable/

.. |made-with-sphinx-doc| image:: https://img.shields.io/badge/Made%20with-Sphinx-1f425f.svg
   :target: https://www.sphinx-doc.org/

.. |Python Versions| image:: https://img.shields.io/pypi/pyversions/pocar

.. |License: MIT| image:: https://img.shields.io/github/license/tiagosarmento/pocar

.. |Release Date| image:: https://img.shields.io/github/release-date/tiagosarmento/pocar

.. |Release Version| image:: https://img.shields.io/github/v/release/tiagosarmento/pocar
   :target: https://github.com/tiagosarmento/pocar/releases/tag/v0.1

.. |Tag Version| image:: https://img.shields.io/github/v/tag/tiagosarmento/pocar
   :target: https://github.com/tiagosarmento/pocar/releases/tag/v0.1

.. |Issues Open| image:: https://img.shields.io/github/issues-raw/tiagosarmento/pocar
   :target: https://github.com/tiagosarmento/pocar/issues

.. |Pypi Version| image:: https://img.shields.io/pypi/v/pocar

.. |Pypi Status| image:: https://img.shields.io/pypi/status/pocar

.. |Pypi License| image:: https://img.shields.io/pypi/l/pocar


|Code QL Analysis| |FLake8 Lint Analysis| |Pytest Analysis|

|Code Style Black| |made-with-sphinx-doc| |Python Versions| |License: MIT|

|Release Date| |Release Version| |Tag Version| |Issues Open|

|Pypi Version| |Pypi Status| |Pypi License|

----

This python package aims to process Open Weather data provided by One Call API response, making it available to end user.

The access to One Call API is free, but an account in Open Weather is required, see: `OpenWeather Account <https://openweathermap.org/full-price#current>`_

See full documentation for One Call API: `One Call API documentation <https://openweathermap.org/api/one-call-api>`_

This package is available in *The Python Package Index (PyPI)* at `Pypi pocar <https://pypi.org/project/pocar/>`_

The One Call API provides the following weather data for any geographical coordinates:

* Current weather
* Minute forecast for 1 hour
* Hourly forecast for 48 hours
* Daily forecast for 7 days
* National weather alerts

This package propose a module to handle each of these kinds of response types.
