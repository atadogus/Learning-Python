import smtplib
import datetime as dt
from random import choice

my_mail_address = "mushiginko14@gmail.com"
password = "Thomas()Mann2.72"

receiving_address = "sule.cavdar@gmail.com"


def send_motivational_mail():
    """This method connects to my email address in order to send a message"""

    try:
        with smtplib.SMTP("smtp.gmail.com", port=587) as new_connection:
            new_connection.starttls()
            new_connection.login(user=my_mail_address, password=password)
            new_connection.sendmail(from_addr=my_mail_address, to_addrs=receiving_address, msg=f"Subject:Motivation\n\n{pick_motivational_message()}")
    except smtplib.SMTPAuthenticationError:
        print("You should check the security settings of your email address")


def pick_motivational_message() -> str:
    """
    This method turns the list of quotes in the text file into a python list and chooses a quote from it
    and returns that quote
    """

    with open("quotes.txt") as quotes_file:
        list_of_quotes = quotes_file.read().split("\n")
        return choice(list_of_quotes)
