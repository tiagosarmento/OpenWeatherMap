import openweathermap
import pytest

# CONSTANT DATA
LAT = 45.1234
LON = 1.2345
KEY = "abcdef1234567890abcdef1234567890"
EXC = "current,daily,minutely,alerts"
URL = f"https://api.openweathermap.org/data/2.5/onecall?lat={LAT}&lon={LON}" f"&exclude={EXC}&units=metric&appid={KEY}"

RAW_DATA_HOURLY = {
    "lat": 43.5832,
    "lon": 7.108,
    "timezone": "Europe/Paris",
    "timezone_offset": 7200,
    "hourly": [
        {
            "dt": 1628690400,
            "temp": 31.52,
            "feels_like": 32.87,
            "pressure": 1016,
            "humidity": 47,
            "dew_point": 18.84,
            "uvi": 5.54,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 2.15,
            "wind_deg": 148,
            "wind_gust": 3.19,
            "weather": [{"id": 800, "main": "Clear", "description": "clear sky", "icon": "01d"}],
            "pop": 0,
        },
        {
            "dt": 1628694000,
            "temp": 30.88,
            "feels_like": 32.23,
            "pressure": 1016,
            "humidity": 49,
            "dew_point": 18.93,
            "uvi": 3.45,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 2.23,
            "wind_deg": 138,
            "wind_gust": 2.38,
            "weather": [{"id": 800, "main": "Clear", "description": "clear sky", "icon": "01d"}],
            "pop": 0,
        },
        {
            "dt": 1628697600,
            "temp": 30.05,
            "feels_like": 31.28,
            "pressure": 1016,
            "humidity": 51,
            "dew_point": 18.81,
            "uvi": 1.7,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 2,
            "wind_deg": 156,
            "wind_gust": 1.91,
            "weather": [{"id": 800, "main": "Clear", "description": "clear sky", "icon": "01d"}],
            "pop": 0,
        },
        {
            "dt": 1628701200,
            "temp": 29.04,
            "feels_like": 30.09,
            "pressure": 1015,
            "humidity": 53,
            "dew_point": 18.49,
            "uvi": 0.59,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 1.29,
            "wind_deg": 155,
            "wind_gust": 1.44,
            "weather": [{"id": 800, "main": "Clear", "description": "clear sky", "icon": "01d"}],
            "pop": 0,
        },
        {
            "dt": 1628704800,
            "temp": 27.5,
            "feels_like": 28.65,
            "pressure": 1016,
            "humidity": 59,
            "dew_point": 18.78,
            "uvi": 0.11,
            "clouds": 1,
            "visibility": 10000,
            "wind_speed": 1.9,
            "wind_deg": 183,
            "wind_gust": 1.97,
            "weather": [{"id": 800, "main": "Clear", "description": "clear sky", "icon": "01d"}],
            "pop": 0,
        },
        {
            "dt": 1628708400,
            "temp": 25.35,
            "feels_like": 25.66,
            "pressure": 1016,
            "humidity": 66,
            "dew_point": 17.9,
            "uvi": 0,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 0.58,
            "wind_deg": 248,
            "wind_gust": 0.78,
            "weather": [{"id": 800, "main": "Clear", "description": "clear sky", "icon": "01n"}],
            "pop": 0,
        },
        {
            "dt": 1628712000,
            "temp": 25.14,
            "feels_like": 25.43,
            "pressure": 1016,
            "humidity": 66,
            "dew_point": 17.64,
            "uvi": 0,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 0.89,
            "wind_deg": 315,
            "wind_gust": 1.3,
            "weather": [{"id": 800, "main": "Clear", "description": "clear sky", "icon": "01n"}],
            "pop": 0,
        },
        {
            "dt": 1628715600,
            "temp": 24.97,
            "feels_like": 25.19,
            "pressure": 1016,
            "humidity": 64,
            "dew_point": 17.05,
            "uvi": 0,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 0.99,
            "wind_deg": 297,
            "wind_gust": 1.59,
            "weather": [{"id": 800, "main": "Clear", "description": "clear sky", "icon": "01n"}],
            "pop": 0,
        },
        {
            "dt": 1628719200,
            "temp": 24.98,
            "feels_like": 25.1,
            "pressure": 1017,
            "humidity": 60,
            "dew_point": 15.92,
            "uvi": 0,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 2.21,
            "wind_deg": 272,
            "wind_gust": 2.86,
            "weather": [{"id": 800, "main": "Clear", "description": "clear sky", "icon": "01n"}],
            "pop": 0,
        },
        {
            "dt": 1628722800,
            "temp": 24.88,
            "feels_like": 24.96,
            "pressure": 1017,
            "humidity": 59,
            "dew_point": 15.3,
            "uvi": 0,
            "clouds": 2,
            "visibility": 10000,
            "wind_speed": 2.27,
            "wind_deg": 303,
            "wind_gust": 2.58,
            "weather": [{"id": 800, "main": "Clear", "description": "clear sky", "icon": "01n"}],
            "pop": 0,
        },
        {
            "dt": 1628726400,
            "temp": 25.01,
            "feels_like": 25.05,
            "pressure": 1017,
            "humidity": 57,
            "dew_point": 14.83,
            "uvi": 0,
            "clouds": 11,
            "visibility": 10000,
            "wind_speed": 2.02,
            "wind_deg": 332,
            "wind_gust": 2.13,
            "weather": [
                {
                    "id": 801,
                    "main": "Clouds",
                    "description": "few clouds",
                    "icon": "02n",
                }
            ],
            "pop": 0,
        },
        {
            "dt": 1628730000,
            "temp": 25.15,
            "feels_like": 25.13,
            "pressure": 1017,
            "humidity": 54,
            "dew_point": 14.19,
            "uvi": 0,
            "clouds": 65,
            "visibility": 10000,
            "wind_speed": 1.76,
            "wind_deg": 11,
            "wind_gust": 2.4,
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04n",
                }
            ],
            "pop": 0,
        },
        {
            "dt": 1628733600,
            "temp": 25.11,
            "feels_like": 25.06,
            "pressure": 1017,
            "humidity": 53,
            "dew_point": 13.94,
            "uvi": 0,
            "clouds": 79,
            "visibility": 10000,
            "wind_speed": 2.38,
            "wind_deg": 35,
            "wind_gust": 3.11,
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04n",
                }
            ],
            "pop": 0,
        },
        {
            "dt": 1628737200,
            "temp": 24.86,
            "feels_like": 24.81,
            "pressure": 1016,
            "humidity": 54,
            "dew_point": 14.08,
            "uvi": 0,
            "clouds": 84,
            "visibility": 10000,
            "wind_speed": 2.58,
            "wind_deg": 33,
            "wind_gust": 3.39,
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04n",
                }
            ],
            "pop": 0,
        },
        {
            "dt": 1628740800,
            "temp": 24.74,
            "feels_like": 24.71,
            "pressure": 1017,
            "humidity": 55,
            "dew_point": 14.11,
            "uvi": 0,
            "clouds": 88,
            "visibility": 10000,
            "wind_speed": 1.97,
            "wind_deg": 34,
            "wind_gust": 2.79,
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04n",
                }
            ],
            "pop": 0,
        },
        {
            "dt": 1628744400,
            "temp": 24.77,
            "feels_like": 24.74,
            "pressure": 1017,
            "humidity": 55,
            "dew_point": 14.17,
            "uvi": 0,
            "clouds": 90,
            "visibility": 10000,
            "wind_speed": 1.91,
            "wind_deg": 34,
            "wind_gust": 2.59,
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04d",
                }
            ],
            "pop": 0,
        },
        {
            "dt": 1628748000,
            "temp": 25.55,
            "feels_like": 25.6,
            "pressure": 1018,
            "humidity": 55,
            "dew_point": 14.54,
            "uvi": 0.52,
            "clouds": 86,
            "visibility": 10000,
            "wind_speed": 2.58,
            "wind_deg": 42,
            "wind_gust": 3.34,
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04d",
                }
            ],
            "pop": 0,
        },
        {
            "dt": 1628751600,
            "temp": 26.76,
            "feels_like": 27.36,
            "pressure": 1018,
            "humidity": 53,
            "dew_point": 14.83,
            "uvi": 1.56,
            "clouds": 18,
            "visibility": 10000,
            "wind_speed": 2.72,
            "wind_deg": 57,
            "wind_gust": 3.48,
            "weather": [
                {
                    "id": 801,
                    "main": "Clouds",
                    "description": "few clouds",
                    "icon": "02d",
                }
            ],
            "pop": 0,
        },
        {
            "dt": 1628755200,
            "temp": 27.41,
            "feels_like": 28.2,
            "pressure": 1018,
            "humidity": 55,
            "dew_point": 15.73,
            "uvi": 3.26,
            "clouds": 16,
            "visibility": 10000,
            "wind_speed": 3.27,
            "wind_deg": 71,
            "wind_gust": 4.29,
            "weather": [
                {
                    "id": 801,
                    "main": "Clouds",
                    "description": "few clouds",
                    "icon": "02d",
                }
            ],
            "pop": 0,
        },
        {
            "dt": 1628758800,
            "temp": 27.67,
            "feels_like": 28.69,
            "pressure": 1019,
            "humidity": 57,
            "dew_point": 16.64,
            "uvi": 5.32,
            "clouds": 11,
            "visibility": 10000,
            "wind_speed": 2.15,
            "wind_deg": 105,
            "wind_gust": 3.05,
            "weather": [
                {
                    "id": 801,
                    "main": "Clouds",
                    "description": "few clouds",
                    "icon": "02d",
                }
            ],
            "pop": 0,
        },
        {
            "dt": 1628762400,
            "temp": 27.97,
            "feels_like": 29.09,
            "pressure": 1019,
            "humidity": 57,
            "dew_point": 17.02,
            "uvi": 7.35,
            "clouds": 11,
            "visibility": 10000,
            "wind_speed": 2.89,
            "wind_deg": 97,
            "wind_gust": 3.61,
            "weather": [
                {
                    "id": 801,
                    "main": "Clouds",
                    "description": "few clouds",
                    "icon": "02d",
                }
            ],
            "pop": 0,
        },
        {
            "dt": 1628766000,
            "temp": 28.17,
            "feels_like": 29.25,
            "pressure": 1019,
            "humidity": 56,
            "dew_point": 17.2,
            "uvi": 8.52,
            "clouds": 18,
            "visibility": 10000,
            "wind_speed": 2.53,
            "wind_deg": 99,
            "wind_gust": 3.43,
            "weather": [
                {
                    "id": 801,
                    "main": "Clouds",
                    "description": "few clouds",
                    "icon": "02d",
                }
            ],
            "pop": 0,
        },
        {
            "dt": 1628769600,
            "temp": 28.33,
            "feels_like": 29.47,
            "pressure": 1019,
            "humidity": 56,
            "dew_point": 17.21,
            "uvi": 8.56,
            "clouds": 30,
            "visibility": 10000,
            "wind_speed": 2.52,
            "wind_deg": 114,
            "wind_gust": 3.2,
            "weather": [
                {
                    "id": 802,
                    "main": "Clouds",
                    "description": "scattered clouds",
                    "icon": "03d",
                }
            ],
            "pop": 0,
        },
        {
            "dt": 1628773200,
            "temp": 28.51,
            "feels_like": 29.6,
            "pressure": 1018,
            "humidity": 55,
            "dew_point": 17.21,
            "uvi": 7.61,
            "clouds": 80,
            "visibility": 10000,
            "wind_speed": 1.87,
            "wind_deg": 132,
            "wind_gust": 2.19,
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04d",
                }
            ],
            "pop": 0,
        },
        {
            "dt": 1628776800,
            "temp": 28.44,
            "feels_like": 29.51,
            "pressure": 1018,
            "humidity": 55,
            "dew_point": 17.02,
            "uvi": 5.68,
            "clouds": 58,
            "visibility": 10000,
            "wind_speed": 2.43,
            "wind_deg": 175,
            "wind_gust": 2.43,
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04d",
                }
            ],
            "pop": 0,
        },
        {
            "dt": 1628780400,
            "temp": 28.21,
            "feels_like": 29.2,
            "pressure": 1018,
            "humidity": 55,
            "dew_point": 16.92,
            "uvi": 3.53,
            "clouds": 50,
            "visibility": 10000,
            "wind_speed": 0.97,
            "wind_deg": 122,
            "wind_gust": 1.88,
            "weather": [
                {
                    "id": 802,
                    "main": "Clouds",
                    "description": "scattered clouds",
                    "icon": "03d",
                }
            ],
            "pop": 0,
        },
        {
            "dt": 1628784000,
            "temp": 28.59,
            "feels_like": 29.48,
            "pressure": 1018,
            "humidity": 53,
            "dew_point": 16.76,
            "uvi": 1.63,
            "clouds": 62,
            "visibility": 10000,
            "wind_speed": 1.33,
            "wind_deg": 41,
            "wind_gust": 2.31,
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04d",
                }
            ],
            "pop": 0,
        },
        {
            "dt": 1628787600,
            "temp": 28.67,
            "feels_like": 29.83,
            "pressure": 1018,
            "humidity": 55,
            "dew_point": 17.3,
            "uvi": 0.56,
            "clouds": 68,
            "visibility": 10000,
            "wind_speed": 0.64,
            "wind_deg": 46,
            "wind_gust": 1.15,
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04d",
                }
            ],
            "pop": 0,
        },
        {
            "dt": 1628791200,
            "temp": 27.83,
            "feels_like": 28.9,
            "pressure": 1018,
            "humidity": 57,
            "dew_point": 17.44,
            "uvi": 0.1,
            "clouds": 73,
            "visibility": 10000,
            "wind_speed": 0.61,
            "wind_deg": 158,
            "wind_gust": 0.93,
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04d",
                }
            ],
            "pop": 0,
        },
        {
            "dt": 1628794800,
            "temp": 27.23,
            "feels_like": 28.07,
            "pressure": 1019,
            "humidity": 56,
            "dew_point": 16.74,
            "uvi": 0,
            "clouds": 99,
            "visibility": 10000,
            "wind_speed": 2.63,
            "wind_deg": 260,
            "wind_gust": 2.84,
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04n",
                }
            ],
            "pop": 0.11,
        },
        {
            "dt": 1628798400,
            "temp": 26.63,
            "feels_like": 26.63,
            "pressure": 1019,
            "humidity": 59,
            "dew_point": 16.95,
            "uvi": 0,
            "clouds": 80,
            "visibility": 10000,
            "wind_speed": 2.42,
            "wind_deg": 275,
            "wind_gust": 2.78,
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04n",
                }
            ],
            "pop": 0.04,
        },
        {
            "dt": 1628802000,
            "temp": 26.49,
            "feels_like": 26.49,
            "pressure": 1018,
            "humidity": 58,
            "dew_point": 16.84,
            "uvi": 0,
            "clouds": 85,
            "visibility": 10000,
            "wind_speed": 2.86,
            "wind_deg": 275,
            "wind_gust": 3.62,
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04n",
                }
            ],
            "pop": 0.11,
        },
        {
            "dt": 1628805600,
            "temp": 26.32,
            "feels_like": 26.32,
            "pressure": 1018,
            "humidity": 59,
            "dew_point": 16.93,
            "uvi": 0,
            "clouds": 78,
            "visibility": 10000,
            "wind_speed": 2.3,
            "wind_deg": 283,
            "wind_gust": 2.89,
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04n",
                }
            ],
            "pop": 0.05,
        },
        {
            "dt": 1628809200,
            "temp": 26.32,
            "feels_like": 26.32,
            "pressure": 1018,
            "humidity": 59,
            "dew_point": 16.87,
            "uvi": 0,
            "clouds": 75,
            "visibility": 10000,
            "wind_speed": 2.5,
            "wind_deg": 283,
            "wind_gust": 3.03,
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04n",
                }
            ],
            "pop": 0.05,
        },
        {
            "dt": 1628812800,
            "temp": 26.08,
            "feels_like": 26.08,
            "pressure": 1019,
            "humidity": 60,
            "dew_point": 16.85,
            "uvi": 0,
            "clouds": 63,
            "visibility": 10000,
            "wind_speed": 2.31,
            "wind_deg": 287,
            "wind_gust": 2.96,
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04n",
                }
            ],
            "pop": 0.03,
        },
        {
            "dt": 1628816400,
            "temp": 25.91,
            "feels_like": 26.12,
            "pressure": 1018,
            "humidity": 60,
            "dew_point": 16.77,
            "uvi": 0,
            "clouds": 2,
            "visibility": 10000,
            "wind_speed": 1.98,
            "wind_deg": 295,
            "wind_gust": 2.42,
            "weather": [{"id": 800, "main": "Clear", "description": "clear sky", "icon": "01n"}],
            "pop": 0,
        },
        {
            "dt": 1628820000,
            "temp": 25.91,
            "feels_like": 26.07,
            "pressure": 1018,
            "humidity": 58,
            "dew_point": 16.31,
            "uvi": 0,
            "clouds": 5,
            "visibility": 10000,
            "wind_speed": 2.5,
            "wind_deg": 314,
            "wind_gust": 2.71,
            "weather": [{"id": 800, "main": "Clear", "description": "clear sky", "icon": "01n"}],
            "pop": 0,
        },
        {
            "dt": 1628823600,
            "temp": 26.09,
            "feels_like": 26.09,
            "pressure": 1018,
            "humidity": 57,
            "dew_point": 16.16,
            "uvi": 0,
            "clouds": 26,
            "visibility": 10000,
            "wind_speed": 2.17,
            "wind_deg": 356,
            "wind_gust": 2.79,
            "weather": [
                {
                    "id": 802,
                    "main": "Clouds",
                    "description": "scattered clouds",
                    "icon": "03n",
                }
            ],
            "pop": 0,
        },
        {
            "dt": 1628827200,
            "temp": 25.76,
            "feels_like": 25.91,
            "pressure": 1018,
            "humidity": 58,
            "dew_point": 16.18,
            "uvi": 0,
            "clouds": 34,
            "visibility": 10000,
            "wind_speed": 1.14,
            "wind_deg": 19,
            "wind_gust": 2.63,
            "weather": [
                {
                    "id": 802,
                    "main": "Clouds",
                    "description": "scattered clouds",
                    "icon": "03n",
                }
            ],
            "pop": 0,
        },
        {
            "dt": 1628830800,
            "temp": 25.5,
            "feels_like": 25.67,
            "pressure": 1018,
            "humidity": 60,
            "dew_point": 16.41,
            "uvi": 0,
            "clouds": 31,
            "visibility": 10000,
            "wind_speed": 0.71,
            "wind_deg": 303,
            "wind_gust": 1.74,
            "weather": [
                {
                    "id": 802,
                    "main": "Clouds",
                    "description": "scattered clouds",
                    "icon": "03d",
                }
            ],
            "pop": 0,
        },
        {
            "dt": 1628834400,
            "temp": 26.69,
            "feels_like": 27.41,
            "pressure": 1019,
            "humidity": 55,
            "dew_point": 16.06,
            "uvi": 0.51,
            "clouds": 35,
            "visibility": 10000,
            "wind_speed": 2.06,
            "wind_deg": 355,
            "wind_gust": 2.21,
            "weather": [
                {
                    "id": 802,
                    "main": "Clouds",
                    "description": "scattered clouds",
                    "icon": "03d",
                }
            ],
            "pop": 0,
        },
        {
            "dt": 1628838000,
            "temp": 27.7,
            "feels_like": 28.46,
            "pressure": 1019,
            "humidity": 54,
            "dew_point": 16.42,
            "uvi": 1.54,
            "clouds": 64,
            "visibility": 10000,
            "wind_speed": 2.8,
            "wind_deg": 37,
            "wind_gust": 3.28,
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04d",
                }
            ],
            "pop": 0,
        },
        {
            "dt": 1628841600,
            "temp": 28.41,
            "feels_like": 29.47,
            "pressure": 1019,
            "humidity": 55,
            "dew_point": 17.12,
            "uvi": 3.24,
            "clouds": 45,
            "visibility": 10000,
            "wind_speed": 3.75,
            "wind_deg": 62,
            "wind_gust": 5.05,
            "weather": [
                {
                    "id": 802,
                    "main": "Clouds",
                    "description": "scattered clouds",
                    "icon": "03d",
                }
            ],
            "pop": 0,
        },
        {
            "dt": 1628845200,
            "temp": 28.59,
            "feels_like": 29.96,
            "pressure": 1020,
            "humidity": 57,
            "dew_point": 17.58,
            "uvi": 5.31,
            "clouds": 37,
            "visibility": 10000,
            "wind_speed": 3.75,
            "wind_deg": 82,
            "wind_gust": 4.84,
            "weather": [
                {
                    "id": 802,
                    "main": "Clouds",
                    "description": "scattered clouds",
                    "icon": "03d",
                }
            ],
            "pop": 0,
        },
        {
            "dt": 1628848800,
            "temp": 28.64,
            "feels_like": 30.17,
            "pressure": 1020,
            "humidity": 58,
            "dew_point": 17.84,
            "uvi": 7.32,
            "clouds": 29,
            "visibility": 10000,
            "wind_speed": 3.44,
            "wind_deg": 97,
            "wind_gust": 4.18,
            "weather": [
                {
                    "id": 802,
                    "main": "Clouds",
                    "description": "scattered clouds",
                    "icon": "03d",
                }
            ],
            "pop": 0,
        },
        {
            "dt": 1628852400,
            "temp": 28.66,
            "feels_like": 30.2,
            "pressure": 1020,
            "humidity": 58,
            "dew_point": 18.01,
            "uvi": 8.5,
            "clouds": 23,
            "visibility": 10000,
            "wind_speed": 3.06,
            "wind_deg": 120,
            "wind_gust": 3.24,
            "weather": [
                {
                    "id": 801,
                    "main": "Clouds",
                    "description": "few clouds",
                    "icon": "02d",
                }
            ],
            "pop": 0,
        },
        {
            "dt": 1628856000,
            "temp": 28.76,
            "feels_like": 30.22,
            "pressure": 1020,
            "humidity": 57,
            "dew_point": 17.83,
            "uvi": 8.54,
            "clouds": 20,
            "visibility": 10000,
            "wind_speed": 2.57,
            "wind_deg": 131,
            "wind_gust": 2.62,
            "weather": [
                {
                    "id": 801,
                    "main": "Clouds",
                    "description": "few clouds",
                    "icon": "02d",
                }
            ],
            "pop": 0,
        },
        {
            "dt": 1628859600,
            "temp": 28.99,
            "feels_like": 30.43,
            "pressure": 1020,
            "humidity": 56,
            "dew_point": 17.66,
            "uvi": 4.05,
            "clouds": 3,
            "visibility": 10000,
            "wind_speed": 1.97,
            "wind_deg": 133,
            "wind_gust": 1.95,
            "weather": [{"id": 800, "main": "Clear", "description": "clear sky", "icon": "01d"}],
            "pop": 0,
        },
    ],
}


def validate_date_func(func, field):
    ocah = openweathermap.OneCallApiHourly(LAT, LON, KEY)
    ocah._rawdata = RAW_DATA_HOURLY
    # case greater than
    with pytest.raises(ValueError):
        func(49)
    # case lesser than
    with pytest.raises(ValueError):
        func(-1)
    # nominal cases value by value
    for idx in range(48):
        assert RAW_DATA_HOURLY["hourly"][idx][field] == func(idx, 1, False)
    # nominal cases all values at once
    values = func(idx, 1, True)
    for idx in range(48):
        assert RAW_DATA_HOURLY["hourly"][idx][field] == values[idx]


def validate_value_func(func, field):
    ocah = openweathermap.OneCallApiHourly(LAT, LON, KEY)
    ocah._rawdata = RAW_DATA_HOURLY
    # case greater than
    with pytest.raises(ValueError):
        func(49)
    # case lesser than
    with pytest.raises(ValueError):
        func(-1)
    # nominal cases value by value
    for idx in range(48):
        assert RAW_DATA_HOURLY["hourly"][idx][field] == func(idx, False)
    # nominal cases all values at once
    values = func(idx, True)
    for idx in range(48):
        assert RAW_DATA_HOURLY["hourly"][idx][field] == values[idx]


def validate_weather_func(func, field):
    ocah = openweathermap.OneCallApiHourly(LAT, LON, KEY)
    ocah._rawdata = RAW_DATA_HOURLY
    # case greater than
    with pytest.raises(ValueError):
        func(49)
    # case lesser than
    with pytest.raises(ValueError):
        func(-1)
    # nominal cases value by value
    for idx in range(48):
        assert RAW_DATA_HOURLY["hourly"][idx]["weather"][0][field] == func(idx, False)
    # nominal cases all values at once
    values = func(idx, True)
    for idx in range(48):
        assert RAW_DATA_HOURLY["hourly"][idx]["weather"][0][field] == values[idx]


# Test: validate constructor nominal case
def test_0000():
    ocah = openweathermap.OneCallApiHourly(LAT, LON, KEY)
    assert ocah.lat == LAT
    assert ocah.lon == LON
    assert ocah.key == KEY
    assert ocah.exc == EXC


# Test: validate method raw data hourly
def test_0001():
    ocah = openweathermap.OneCallApiHourly(LAT, LON, KEY)
    ocah._rawdata = RAW_DATA_HOURLY
    assert ocah.raw_data_hourly() == RAW_DATA_HOURLY["hourly"]


# Test: validate method data_time
def test_0002():
    ocah = openweathermap.OneCallApiHourly(LAT, LON, KEY)
    ocah._rawdata = RAW_DATA_HOURLY
    validate_date_func(ocah.data_time, "dt")


# Test: validate method temp
def test_0003():
    ocah = openweathermap.OneCallApiHourly(LAT, LON, KEY)
    ocah._rawdata = RAW_DATA_HOURLY
    validate_value_func(ocah.temp, "temp")


# Test: validate method feels_like
def test_0004():
    ocah = openweathermap.OneCallApiHourly(LAT, LON, KEY)
    ocah._rawdata = RAW_DATA_HOURLY
    validate_value_func(ocah.feels_like, "feels_like")


# Test: validate method pressure
def test_0005():
    ocah = openweathermap.OneCallApiHourly(LAT, LON, KEY)
    ocah._rawdata = RAW_DATA_HOURLY
    validate_value_func(ocah.pressure, "pressure")


# Test: validate method humidity
def test_0006():
    ocah = openweathermap.OneCallApiHourly(LAT, LON, KEY)
    ocah._rawdata = RAW_DATA_HOURLY
    validate_value_func(ocah.humidity, "humidity")


# Test: validate method dew_point
def test_0007():
    ocah = openweathermap.OneCallApiHourly(LAT, LON, KEY)
    ocah._rawdata = RAW_DATA_HOURLY
    validate_value_func(ocah.dew_point, "dew_point")


# Test: validate method uvi
def test_0008():
    ocah = openweathermap.OneCallApiHourly(LAT, LON, KEY)
    ocah._rawdata = RAW_DATA_HOURLY
    validate_value_func(ocah.uvi, "uvi")


# Test: validate method clouds
def test_0009():
    ocah = openweathermap.OneCallApiHourly(LAT, LON, KEY)
    ocah._rawdata = RAW_DATA_HOURLY
    validate_value_func(ocah.clouds, "clouds")


# Test: validate method visibility
def test_0010():
    ocah = openweathermap.OneCallApiHourly(LAT, LON, KEY)
    ocah._rawdata = RAW_DATA_HOURLY
    validate_value_func(ocah.visibility, "visibility")


# Test: validate method wind_speed
def test_0011():
    ocah = openweathermap.OneCallApiHourly(LAT, LON, KEY)
    ocah._rawdata = RAW_DATA_HOURLY
    validate_value_func(ocah.wind_speed, "wind_speed")


# Test: validate method wind_deg
def test_0012():
    ocah = openweathermap.OneCallApiHourly(LAT, LON, KEY)
    ocah._rawdata = RAW_DATA_HOURLY
    validate_value_func(ocah.wind_deg, "wind_deg")


# Test: validate method wind_gust
def test_0013():
    ocah = openweathermap.OneCallApiHourly(LAT, LON, KEY)
    ocah._rawdata = RAW_DATA_HOURLY
    validate_value_func(ocah.wind_gust, "wind_gust")


# Test: validate method weather_id
def test_0014():
    ocah = openweathermap.OneCallApiHourly(LAT, LON, KEY)
    ocah._rawdata = RAW_DATA_HOURLY
    validate_weather_func(ocah.weather_id, "id")


# Test: validate method weather_main
def test_0015():
    ocah = openweathermap.OneCallApiHourly(LAT, LON, KEY)
    ocah._rawdata = RAW_DATA_HOURLY
    validate_weather_func(ocah.weather_main, "main")


# Test: validate method weather_description
def test_0016():
    ocah = openweathermap.OneCallApiHourly(LAT, LON, KEY)
    ocah._rawdata = RAW_DATA_HOURLY
    validate_weather_func(ocah.weather_description, "description")


# Test: validate method weather_icon
def test_0017():
    ocah = openweathermap.OneCallApiHourly(LAT, LON, KEY)
    ocah._rawdata = RAW_DATA_HOURLY
    validate_weather_func(ocah.weather_icon, "icon")


# Test: validate method pop
def test_0018():
    ocah = openweathermap.OneCallApiHourly(LAT, LON, KEY)
    ocah._rawdata = RAW_DATA_HOURLY
    validate_value_func(ocah.pop, "pop")
