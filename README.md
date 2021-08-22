# POCAR - Process One Call Api Response
---

![Code QL Analysis](https://github.com/tiagosarmento/pocar/actions/workflows/codeql-analysis.yml/badge.svg)
![FLake8 Lint Analysis](https://github.com/tiagosarmento/pocar/actions/workflows/flake8-analysis.yml/badge.svg)
![Pytest Analysis](https://github.com/tiagosarmento/pocar/actions/workflows/pytest-analysis.yml/badge.svg)

![Code Style Black](https://img.shields.io/badge/code%20style-black-000000.svg)
![License: MIT](https://img.shields.io/github/license/tiagosarmento/pocar)

![Release Date](https://img.shields.io/github/release-date/tiagosarmento/pocar)
![Release Version](https://img.shields.io/github/v/release/tiagosarmento/pocar)
![Tag Version](https://img.shields.io/github/v/tag/tiagosarmento/pocar)

---

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
