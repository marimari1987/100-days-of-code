import requests
from datetime import datetime
import smtplib
import time

MY_LAT_POS = <insertlat>
MY_LONG_POS = <insertlon>
MY_EMAIL = "mymail@mail.com"
PASSWORD = "mypassword"


def is_iss_overhead():
    # API request, ein Application Programming Interface ist sozusagen ein Banker, der die Bank verwaltet
    # oder eine Bedienung im Restaurant, die einem das Menü zeigt

    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")  # <Response [200]>
    # print(response.status_code)  # 200
    # invalid_response = requests.get(url="http://api.open-notify.org/das-geht-nicht.json")  # <Response [404]>
    # if response.status_code == 404:
    #     raise Exception("That resource does not exist")
    # elif response.status_code == 401:
    #     raise Exception("You are not authorized to access")

    # Damit das automatisch gemacht wird:

    # print(invalid_response)
    response_iss.raise_for_status()  # raise HTTPError(http_error_msg, response=self) requests.
    # # exceptions.HTTPError: 404 Client Error: Not Found for url:

    data_iss = response_iss.json()  # {'message': 'success', 'iss_position': {'longitude': '114.3829', 'latitude': '17.9175'}, 'timestamp': 1621247971}
    iss_longitude = float(data_iss["iss_position"]["longitude"])
    iss_latitude = float(data_iss["iss_position"]["latitude"])

    if MY_LONG_POS - 5 < iss_longitude < MY_LONG_POS + 5 and MY_LAT_POS - 5 < iss_latitude < MY_LAT_POS + 5:  # Position kann +/- 5 sein, damit man die ISS sieht
        return True
    else:
        return False
    # print(iss_longitude)
    # Um sich die Position anzeigen zu lassen:
    # https://www.latlong.net/Show-Latitude-Longitude.html  (Geographic Tools eingeben, dass man Long und latitude to adress möchte)

# Sunrise and Sunset so that it's dark enough to see the iss on sky, formatted ändert das Zeitformat von AM und PM auf
# 2021-05-19T03:25:30+00:00


def is_night():
    parameters = {"lat": MY_LAT_POS,
                  "lng": MY_LONG_POS,
                  "formatted": 0

    }

    response_sr_ss = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response_sr_ss.raise_for_status()
    data_sunrise_and_set = response_sr_ss.json()
    sunrise = data_sunrise_and_set["results"]["sunrise"]
    sunset = data_sunrise_and_set["results"]["sunset"]
    hour_now = datetime.now().hour  # Falls man nicht in der UTC timezone lebt: from datetime import datetime, timezone
    # datetime.now(timezone.utc)
    sunset_hour = int(sunset.split("T")[1].split(":")[0])  # Urpsrüngliches Format nach formatted = 0 : 2021-05-19T17:03:29
    sunrise_hour = int(sunrise.split("T")[1].split(":")[0])

    if sunset_hour <= hour_now <= sunrise_hour:  # wenn es nacht ist
        return True
    else:
        return False


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg="Subject:Schau nach Oben\n\n"
                                    "Die ISS ist gerade am Himmel zu sehen"
                                )

