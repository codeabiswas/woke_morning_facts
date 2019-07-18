import requests
from datetime import date


todayMonth = date.today().strftime("%m")
todayDay = date.today().strftime("%d")

if todayDay[0] == '0':
    todayDay = todayDay[1]

if todayMonth[0] == '0':
    todayMonth = todayMonth[1]

# API-Endpoint
url = "http://numbersapi.com/" + todayMonth + "/" + todayDay + "/date?json"

# Get the response object
factResponse = requests.get(url = url)

fact = factResponse.json()["text"]

print(fact)