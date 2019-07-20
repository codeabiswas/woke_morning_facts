from datetime import date
import time
import requests
import spotipy
import random

# Author:       Andrei Biswas
# GitHub:       codeabiswas
# Email:        petitendian@gmail.com

# Created on:   Tuesday, July 18, 2019
# Modified on:  Tuesday, July 19, 2019

"""
    Sets the alarm and prints a fun fact when the alarm "rings"
"""
def setAlarm(alarmTime, artistNames, spotifyToken):

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
            
            artistIndex = random.randint(0, len(artistNames)-1)
                      
            spotify = spotipy.Spotify(auth=spotifyToken)
            results = spotify.search(q=artistNames[artistIndex], limit=20)

            trackList = []

            for t in results['tracks']['items']:
                print(t['name'])
                # Used for the JS module
                spotifyURI = "spotify:track:"+t['id']
                trackList.append(spotifyURI)

            trackIndex = random.randint(0, len(artistNames)-1)
            trackURI = trackList[trackIndex]
            print(trackURI)
            
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
    alarmTime = "04:29 AM"

    artistNames = ["Coldplay", "Madeon", "Lido", "The 1975"]

    spotifyToken = 'BQA6NgWO9JPDY7xcN3TTmPJ_4rZZH10zv699udJyGFr9J0VCq6K3_SMEhvhWXk_5PUHw5MDnCrHGYZk4jqtMQ0kXOoRe-T45DSmham_Fb_GL8-lWkoWi1FvlYItugSkXz-weNesHk2JhHgaRTBjCDUlwZId_pxyWB3EhKb-oYQ'

    setAlarm(alarmTime, artistNames, spotifyToken)