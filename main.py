from datetime import date
from flask import Flask
from multiprocessing import Process, Value
import time
import requests
import spotipy
import random
from spotipy.oauth2 import SpotifyClientCredentials
import vlc
import pafy

# Author:       Andrei Biswas
# GitHub:       codeabiswas
# Email:        petitendian@gmail.com

# Created on:   Tuesday, July 18, 2019
# Modified on:  Saturday, July 27, 2019

"""
    Sets the alarm and prints a fun fact when the alarm "rings"
"""
def setAlarm(alarmTime, youtubeURL):

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

            ringProcess = Process(target=ringAlarm, args=(youtubeURL,))
            ringProcess.start()

            # Update the time            
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

    # Fetch the fact from the JSON objectDDidDidDidid
    fact = factResponse.json()["text"]

    return fact


"""
    Play music for the alarm ringtone
"""
def ringAlarm(youtubeURL):
    
    # Get the video object
    video = pafy.new(youtubeURL)
    # Get the best audio from the youtube URL
    best = video.getbest()
    
    # Fetch a VLC Instance
    instance = vlc.Instance()
    # Create a new VLC player
    player = instance.media_player_new()
    # Get the media object
    media = instance.media_new(best.url)
    # Get the media objects MRL
    media.get_mrl()
    # Set the player to play the media object
    player.set_media(media)

    # Start playing the media
    player.play()

if __name__ == "__main__":

    youtubeURL = "https://youtu.be/qQWAicHiVhk"

    # Set the alarm time
    alarmTime = "06:10 PM"

    setAlarm(alarmTime, youtubeURL)