import requests

URL = "https://thispersondoesnotexist.com"


""" --- THIS FUNCTION IS FOR GETTING IMAGES FOR THE ACCOUNT --- """
def get_image():
    response = requests.get(url=URL)
    with open("image.jpg", "wb") as file:
        file.write(response.content)