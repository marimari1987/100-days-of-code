import pandas
import datetime as dt
import random
import smtplib

# Wenn man das Programm in der Cloud täglich laufen lassen will:
# https://www.pythonanywhere.com/
# account kreiren und drauf achten, dass der relative file path gleich bleibt mit dem Ordenr letter_templates
# Anleitung: https://www.udemy.com/course/100-days-of-code/learn/lecture/21110124#questions

my_mail = "mymail@mail.de"
password = "mypassword"

birthday_data = pandas.read_csv("birthdays.csv")
data = pandas.DataFrame(birthday_data)
data_dict = data.to_dict(orient="records")

now = dt.datetime.now()

for person in data_dict:
    if person["month"] == now.month and person["day"] == now.day:
        print(person["email"])
        letter_number = random.randint(1, 3)
        random_letter = f"letter_{letter_number}.txt"
        with open(f"letter_templates/{random_letter}") as letter:
            text = letter.read()
            personalized_text = text.replace("[NAME]", person["name"])  # WICHTIG: Variable vergeben!
        with smtplib.SMTP("smtp.mail.yahoo.de") as connection:
            connection.starttls()
            connection.login(user=my_mail, password=password)
            connection.sendmail(from_addr=my_mail,
                                to_addrs=person["email"],
                                msg=f"Subject: Happy Birthday!\n\n{personalized_text}")

# Musterlösung:
# now = dt.datetime.now()
# today_tuple = (now.month, now.day)
#
# birthday_dict = {(data_row.month, data_row.day): data_row
#                  for (item, data_row) in birthday_data.iterrows()}
#
# if today_tuple in birthday_dict:
#     person_name = birthday_dict[today_tuple]["name"]
#     person_email = birthday_dict[today_tuple]["email"]
#     letter_number = random.randint(1, 3)
#     random_letter = f"letter_{letter_number}.txt"
#     with open(f"letter_templates/{random_letter}") as letter:
#         text = letter.read()
#         personalized_text = text.replace("[NAME]", person_name)
#     with smtplib.SMTP("smtp.server) as connection:
#         connection.starttls()
#         connection.login(user=my_mail, password=password)
#         connection.sendmail(from_addr=my_mail,
#                             to_addrs=person_email,
#                             msg=f"Subject: Happy Birthday!\n\n{personalized_text}")