import os
import re
import requests
from pprint import pprint


#get image
URL = "https://thispersondoesnotexist.com"
TEMP_MAIL_BASE = "https://api.mail.tm"


def get_image():
    response = requests.get(url=URL)
    with open("image.jpg", "wb") as file:
        file.write(response.content)


def get_temp_mail():
    response = requests.get(f"{TEMP_MAIL_BASE}/domains")
    domain = response.json()["hydra:member"][0]["domain"]
    return domain

def create_account():
    email = f"mytempmail@{get_temp_mail()}"
    password = os.environ[""]


pprint(get_temp_mail())




