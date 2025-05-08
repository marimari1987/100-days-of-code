import requests
from dotenv import load_dotenv
import os
from twilio.rest import Client


appid_key = os.getenv("OWM_API_KEY")

# print(os.environ.get("TEST")  # eingegeben mit setx TEST "ja" Damit könnte man auch die API Keys eingeben

# Wenn man den falschen Key eingibt: Err 401 (unauthorized)

MY_LAT = <insertlat>
MY_LON = <insertlon>

# https://www.twilio.com/console
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")

parameters = {"lat": MY_LAT,
              "lon": MY_LON,
              "units": "metric",
              "appid": appid_key,
              "exclude": "current,minutely,daily"
              }
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()  # Das NICHT VERGESSEN
weather_data_48 = response.json()["hourly"]  # stündlich für 48 Stunden
weather_data_24 = weather_data_48[:23]
# Online JSON Viewer: http://jsonviewer.stack.hu/
# {
#   'lat': <insert lat>,
#   'lon': <insert lon>,
#   'timezone': <insert timezone>,
#   'timezone_offset': 7200,
#   'hourly': [
#     {
#       'dt': 1621764000,
#       'temp': 12.36,
#       'feels_like': 11.22,
#       'pressure': 1014,
#       'humidity': 60,
#       'dew_point': 4.82,
#       'uvi': 4.26,
#       'clouds': 83,
#       'visibility': 10000,
#       'wind_speed': 6.91,
#       'wind_deg': 253,
#       'wind_gust': 9.84,
#       'weather': [
#         {
#           'id': 803,
#           'main': 'Clouds',
#           'description': 'broken clouds',
#           'icon': '04d'
#         }
#       ],
#       'pop': 0.33
#     },
#     {
#       'dt': 1621767600, ....
# weather_data = weather_data_48["hourly"][0]["weather"]
# [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}]
# id Codes:
# https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2
# print(weather_data_48[0]["dt"])  # https://www.unixtimestamp.com/  converter von unix time
will_rain = False
will_freeze = False
text = ""
maybe = "nicht"

for hour in range(1, 12):
    print(weather_data_48[hour]["weather"][0]["id"])
    if 300 <= weather_data_48[hour]["weather"][0]["id"] < 600:
        time_from_now = (weather_data_48[hour]["dt"] - weather_data_48[0]["dt"])/3600
        text += f"Es regnet heute in {int(time_from_now)} Stunden.\n"
        will_rain = True
for hour in weather_data_24:
    if hour["temp"] < 1:
        maybe = ""
        will_freeze = True
text += f"Heute friert es {maybe}."

if will_freeze or will_rain:
    print(text)

