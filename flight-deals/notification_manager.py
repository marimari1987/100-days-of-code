import smtplib

my_email = "myemail"
password = "mypassword"

class NotificationManager:

    def send_email(self, text, user_email):
        with smtplib.SMTP("smtpserver") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=user_email,
                                msg=f"Subject:Flug Deal von Annika\n\n{text}")

