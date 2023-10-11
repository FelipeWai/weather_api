import requests
from pprint import pprint
from api_key import api_key

# city = input("Dogite a cidade: ")

base_url = "http://api.weatherapi.com/v1/current.json?"

param = {
    "key": api_key,
    "q": 'Santos',
    "days": '6',
    "lang": "pt"
}

response = requests.get(base_url, params=param)

pprint(response.json())

