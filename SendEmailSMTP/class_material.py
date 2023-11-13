import smtplib
import datetime as dt

my_mail_address = "mushiginko14@gmail.com"
password = "Thomas()Mann2.72"

receiving_address = "witcherginko@gmail.com"

new_connection = smtplib.SMTP("smtp.gmail.com", port=587)
new_connection.starttls()
new_connection.login(user=my_mail_address, password=password)
new_connection.sendmail(from_addr=my_mail_address, to_addrs=receiving_address, msg="Subject:Greeting\n\nHello")
new_connection.close()

with smtplib.SMTP("smtp.gmail.com", port=587) as new_connection:
    new_connection.starttls()
    new_connection.login(user=my_mail_address, password=password)
    new_connection.sendmail(from_addr=my_mail_address, to_addrs=receiving_address, msg="Subject:Greeting\n\nHello")

# it is the same code as the one above


now = dt.datetime.now()
year = now.year
month = now.month
weekday = now.weekday()
print(type(now))
print(weekday)

date_of_birth = dt.datetime(year=1998, month=1, day=8)