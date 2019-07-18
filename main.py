import requests
from datetime import date

# Fetch today's day and month
todayDay = date.today().strftime("%d")
todayMonth = date.today().strftime("%m")

# Format the day and month
if todayDay[0] == '0':
    todayDay = todayDay[1]

if todayMonth[0] == '0':
    todayMonth = todayMonth[1]

# API-Endpoint
url = "http://numbersapi.com/" + todayMonth + "/" + todayDay + "/date?json"

# Get the response object
factResponse = requests.get(url = url)

# Fetch the fact from the JSON object
fact = factResponse.json()["text"]

# Print out the fact
print(fact)