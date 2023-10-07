import requests

URL = " https://islomapi.uz/api/present/day?region=Toshkent"
data = requests.get(URL)

for i in data:
    