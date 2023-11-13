import requests
import smtplib
from time import sleep

MY_LATITUDE: float = 41.03
MY_LONGITUDE: float = 29.18

MY_EMAIL = "yesWEcan@gmail.com"
MY_PASSWORD = "YesWeCan1407"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

current_iss_longitude = round(float(data["iss_position"]["longitude"]), 2)
current_iss_latitude = round(float(data["iss_position"]["latitude"]), 2)
current_iss_position = (current_iss_longitude, current_iss_latitude)


def send_mail():
    """Sends an email to inform me that I may see the ISS if I loop up at the sky"""

    try:
        with smtplib.SMTP("smtp.gmail.com", port=587) as new_connection:
            new_connection.starttls()
            new_connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            new_connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                                    msg=f"Subject:ISS Message\n\nLook up, the ISS is passing by")
    except smtplib.SMTPAuthenticationError:
        print("You should check the security settings of your email address")


def main():

    iss_on_spot = False
    while iss_on_spot is False:
        if MY_LATITUDE - 1 <= current_iss_latitude <= MY_LATITUDE + 1 and MY_LONGITUDE - 1 <= current_iss_longitude <= MY_LONGITUDE + 1:
            send_mail()
            iss_on_spot = True
        else:
            print(current_iss_position)

        sleep(60.0)


if __name__ == "__main__":
    main()
