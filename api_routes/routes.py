
import requests

base_url = "https://api.thecatapi.com/v1"

def get_gatos():
    url = f"{base_url}/breeds"

    headers = {
        "x-api-key": "live_ABUGf6IVIuX95IG92cDoXsJS6A50z5f8QZl6MvfDBEpt7Teakp1F1VCcQ9PlO8mi"
    }

    resposta = requests.get(url, headers=headers)

    return resposta.json()

def get_image():
    url = f"https://api.thecatapi.com/v1/images/search"

    resposta = requests.get(url)

    return resposta.json()[0]