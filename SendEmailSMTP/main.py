import smtplib
import datetime as dt
import csv
from random import randint

MY_EMAIL_ADDRESS = "mushiginko14@gmail.com"
PASSWORD = "Thomas()Mann2.72"


def scan_for_birthdays() -> dict:
    """Scans the csv file to see whether today is somebody's birthday"""

    with open("birthdays.csv") as csv_birthdays:
        birthdays_dict = csv.DictReader(csv_birthdays)
        for row in birthdays_dict:
            try:
                if int(row["month"]) == dt.datetime.now().month and int(row["day"]) == dt.datetime.now().day:
                    return {"name": row["name"], "email": row["email"]}
            except TypeError:
                pass


def pick_birthday_message() -> str:
    """Picks a birthday message from templates"""

    with open(f"letter_templates/letter_{randint(1,3)}.txt") as birthday_text:
        return birthday_text.read()


def send_birthday_mail(info: dict):
    """Sends a congratulations email to the birthday boy/girl"""

    receiving_address = info["email"]
    birthday_message = pick_birthday_message().replace("[NAME]", info["name"])

    try:
        with smtplib.SMTP("smtp.gmail.com", port=587) as new_connection:
            new_connection.starttls()
            new_connection.login(user=MY_EMAIL_ADDRESS, password=PASSWORD)
            new_connection.sendmail(from_addr=MY_EMAIL_ADDRESS, to_addrs=receiving_address, msg=f"Subject:Birthday Message\n\n{birthday_message}")
    except smtplib.SMTPAuthenticationError:
        print("You should check the security settings of your email address")


def main():

    birthday_boy = scan_for_birthdays()
    if birthday_boy is not None:
        send_birthday_mail(birthday_boy)


if __name__ == "__main__":
    main()
