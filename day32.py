# import smtplib
#
import smtplib

my_email = "mymail@mail.com"  # identity of email: elgoogtest3, id of provider:gmail.com
password = "mypassword"
#
# with smtplib.SMTP("smtp.server") as connection:  # SMTP Objekt (SMTP ist quasi der "Postbote, der die Emails verteilt)
#     connection.starttls()  # tls = Transport Layer Security end-to-end verschlüsselung
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="elgoogtest3@gmail.com",
#                         msg="Subject:Hello\n\nThis is the E-Mail body")
# connection.close()  # wie bei with open, braucht man es in dieser Form nicht
# damit das Senden funktioniert, muss man in den Sicherheiteinstellungen Apps mit weniger sicherheit erlauben
# Wenn man von yahoo senden möchte, muss man in den sicherheitseinstellungen ein neues Passwort für diese "App" anlegen

import datetime as dt
import random

now = dt.datetime.now()  # 2021-05-16 14:03:31.594722 type: <class 'datetime.datetime'>
# year = now.year  # 2021 type: <class 'int'>
# day_of_the_week = now.weekday()  # 1 (bedeutet es ist Dienstag, Montag wäre 0)
#
# date_of_birth = dt.datetime(year=1987, month=6, day=25)  # 1987-06-25 00:00:00 (die Uhrzeit ist default)

if now.weekday() == 0:
    with open("quotes.txt") as data_file:
        data_list = data_file.readlines()
        random_quote = random.choice(data_list)
    with smtplib.SMTP("smtp.server") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:Weekly motivational quote\n\n{random_quote}"
                            )


