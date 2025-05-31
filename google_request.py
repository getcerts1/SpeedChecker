import os
import requests
from dotenv import load_dotenv

load_dotenv()


def google_request():
    query = "internet speed test"
    url = f"https://www.googleapis.com/customsearch/v1?key={os.getenv("API_KEY")}&cx={os.getenv("SEARCH_ENGINE_ID")}&q={query}"

    response = requests.get(url)
    data = response.json()

    links = [item["link"] for item in data.get("items", [])]
    return links




