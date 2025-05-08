import requests
from datetime import datetime

USERNAME = <username>
TOKEN = <token>

# # https://pixe.la/
# paramters = {
#     "token": TOKEN,  # selbst ausgedachter Token
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
#
pixela_endpoint = "https://pixe.la/v1/users"
#
# ## Neuen Account machen:
# # response = requests.post(url=pixela_endpoint, json=paramters)
# # print(response.text)  # {"message":"This user already exist.","isSuccess":false}
# # {"message":"Success. Let's visit https://pixe.la/@ank , it is your profile page!","isSuccess":true}
#
# ## create a graph:
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
# # Validation rule id: ^[a-z][a-z0-9-]{1,16} erst ein buchstabe, dann buchstaben der zahlen, muss 1 - 16
# header = {
#      "X-USER-TOKEN": TOKEN
#  }
# graph_params_body = {
#     "id": "graph1",
#     "name": "Coding Hours Graph",
#     "unit": "hours",
#     "type": "int",
#     "color": "ajisai"
# }
#
# # response = requests.post(url=graph_endpoint, headers=header, json=graph_params_body)
# # print(response.text)
# # https://pixe.la/v1/users/ank/graphs/graph1.html

## post into the graph
## Datum formatieren mit split und join:
# today = str(datetime.now().date())
# today_formated = today.split("-")
# print("".join(today_formated))

## Datum formatieren mit dateteime:
today = datetime.now()
today_formated = today.strftime("%Y%m%d")  # 20210531
# %y (klengeschrieben gibt das Jahr als 21 aus,  als einstellige Zahl, %Y als 2021
# alternativ geht es auch mit arrow:
# today_date = arrow.now().format('YYYYMMDD')

graph_id = "graph1"
# post_endpoint = f"{graph_endpoint}/{graph_id}"
# post_params = {
#     "date": "20210529",
#     "quantity": "2"
# }
#
# response = requests.get(url=post_endpoint, headers=header, json=post_params)
# print(response.text)
# print(post_endpoint)  # Kommt eine Fehlermeldung... klappt nicht
# Fehler gefunden: requests.get() funktioniert natrlich nicht, es muss natürlich requests.post() sein


header = {
    "X-USER-TOKEN": TOKEN
}
set_pixel = {
    "date": today_formated,
    "quantity": input("Wie viele Stunden hat die Übung gedauert?\n")
}
set_pixel_2 = {
    "date": "20210529",
    "quantity": "2"
}
set_pixel_3 = {
    "date": "20210528",
    "quantity": "5"
}
response = requests.post(url=f"{pixela_endpoint}/ank/graphs/graph1", headers=header, json=set_pixel)
print(response.text)

## Update a pixel:
update_pixel_3 = {
    "quantity": "2"
}
modifying_date = set_pixel_3["date"]
# response = requests.put(url=f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}/{modifying_date}", headers=header, json=update_pixel_3)
# print(response.text)

## Delete a pixel:
# response = requests.delete(url=f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}/{today_formated}", headers=header)
# print(response.text)

## Delete a user:
# delete_token_header = {
#       "X-USER-TOKEN": "dasistmeintoken"
# }
# response = requests.delete(url=f"{pixela_endpoint}/neuername2", headers=delete_token_header)
# print(response.text)
