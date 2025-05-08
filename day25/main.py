# with open("weather_data.csv") as data_file:
#     data_list = data_file.readlines()
#     print(data_list)
## in dieser Version müsste man viele umwandlungen machen, um an die Daten heranzukmmen
## daher ide ienfachere Methode:

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)  # kreiert ein csv Objekt mit verschiednen Reihen
#     temperatures = []
#     for row in data:
#         # print(row)  # jede Reihe enthält nun eine Liste mit den unterschiedlichen Einträgen
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
# print(temperatures)
#
# # das ist immernoch etwas aufwenig, deshlab Pandas:

import pandas

# data = pandas.read_csv("weather_data.csv")  # macht automatisch eine Tabelle
# print(type(data))  # <class 'pandas.core.frame.DataFrame'>
# print(data["temp"])  # hiermit kann man gleich eine bestimmte Spalte auswählen
# print(type(data["temp"])) # <class 'pandas.core.series.Series'>
# data_dict = data.to_dict()
# print(data_dict)  # macht ein dictionary aus den daten
# temp_list = data["temp"].to_list()
# print(temp_list)  # macht eine Liste mit den Temperaturen

# average = 0
# for temperature in temp_list:
#     average += temperature
# average /= len(temp_list)
## schneller:
# average_temperature = sum(temp_list)/len(temp_list)
# print(average_temperature)
# # oder mit pandas:
# average = data["temp"].mean()
# print(average)
# maximum_temp = data["temp"].max()
# print(maximum_temp)

# Man bruacht nichtmal mit den eckigen Klammern zu arbeiten:
# print(data.condition)
# Pandas macht aus jeder Zeilenüberschirft automatisch ein Klassenattribut
# sodass jede Spalte direkt abrufbar ist

# eine Spalte ausgeben:
# print(data[data.day == "Monday"])
# mit den Eckigen Klammern und einer condition darin, kann mna eine Reihe ansprechen

# line_highest_temperature = data[data.temp == data.temp.max()]
# print(line_highest_temperature)

## man kann auch die einzelen Werte einer Reihe abfragen:

# monday = data[data.day == "Monday"]
# print(monday.condition)
# temperature_monday = monday.temp
# temperature_in_fahrenheit = temperature_monday * 1.8 + 32
# print(temperature_in_fahrenheit)

## Mit Pandas daten erstellen:
# data_dict = {"students": ["Amy", "James", "Angela"],
#              "scores": [76, 56, 65]
#              }
# data = pandas.DataFrame(data_dict)
# print(data)
#
# data.to_csv("new_data.csv")

data = pandas.read_csv("squirrel_data.csv")
fur_colors_list = data["Primary Fur Color"].to_list()
fur_colors_dict = {}
for fur_color in fur_colors_list:
    if fur_color not in fur_colors_dict:
        fur_colors_dict[fur_color] = 0
    else:
        fur_colors_dict[fur_color] += 1

fur_colors_distribution = {"Fur Color" : [], "number" : []}
for color in fur_colors_dict:
    fur_colors_distribution["Fur Color"].append(color)
    fur_colors_distribution["number"].append(fur_colors_dict[color])

print(fur_colors_distribution)

new_data = pandas.DataFrame(fur_colors_distribution)
new_data.to_csv("fur_color_distribution")

# data = pandas.DataFrame(fur_colors_dict)
# data.to_csv("fur_color_distribution")
