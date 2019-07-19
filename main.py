from datetime import date
import time
import requests
import spotipy

# Author:       Andrei Biswas
# GitHub:       codeabiswas
# Email:        petitendian@gmail.com

# Created on:   Tuesday, July 18, 2019
# Modified on:  Tuesday, July 19, 2019

"""
    Sets the alarm and prints a fun fact when the alarm "rings"
"""
def setAlarm(alarmTime):

    # Get AM/PM
    dayOrNight = alarmTime[6:]
    
    # Set the alarm time to exact :00 seconds
    alarmTime = alarmTime[0:5] + ":00 " + dayOrNight
    
    # Get the current time
    currTime = time.strftime("%I:%M:%S %p")

    # Run forever
    while True:
        # Until it is time for the alarm, just keep printing the current time
        if (currTime != alarmTime):
            currTime = time.strftime("%I:%M:%S %p")
            print("Current Time: ", currTime)
            time.sleep(1)

        else:
            print(fetchFact())
            
            token = "BQDOcXu2_0I1uxggAFviQK9-f5FFiy2qfnkcJdg-OyamaSEeem-sBN2IXxi8nHagelFc50RL5HQMN9G3ZRmiGVccfA9AbkPUocmzdGHV_fybjKrUDExUDshqDTKKsw3oBoV-5Y5C7YoGwQOdmZRnpxWoEo-1j-zWf8zjCG6UEw"
            spotify = spotipy.Spotify(auth=token)
            results = spotify.search(q="Coldplay", limit=20)
            for i, t in enumerate(results['tracks']['items']):
                print('',str(int(i)+1),t['name'])
                # Used for the JS module
                spotify_uri = "spotify:track:"+t['id']
                print(spotify_uri)
            currTime = time.strftime("%I:%M:%S %p")
"""
    Fetch a fact given the date
"""
def fetchFact():

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

    return fact

if __name__ == "__main__":

    # Set the alarm time
    alarmTime = "12:11 AM"

    # Start the alarm
    setAlarm(alarmTime)