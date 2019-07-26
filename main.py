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
# Modified on:  Tuesday, July 20, 2019

app = Flask(__name__)

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

            # Get the video object
            video = pafy.new(youtubeURL)
            # Get the best audio from the youtube URL
            best = video.getbestaudio()
            
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

@app.route('/')
def spotifyPlayerPage():
    return """
    <html>
    <head>
    <title>Embedded Endian Device Spotify Player</title>
    </head>
    <body>
    <h1>Embedded Endian Device Spotify Player</h1>
    <h2>Open your console log: <code>View > Developer > JavaScript Console</code></h2>

    <script src="https://sdk.scdn.co/spotify-player.js"></script>
    <script>
        window.onSpotifyWebPlaybackSDKReady = () => {
        const token = 'BQA6NgWO9JPDY7xcN3TTmPJ_4rZZH10zv699udJyGFr9J0VCq6K3_SMEhvhWXk_5PUHw5MDnCrHGYZk4jqtMQ0kXOoRe-T45DSmham_Fb_GL8-lWkoWi1FvlYItugSkXz-weNesHk2JhHgaRTBjCDUlwZId_pxyWB3EhKb-oYQ';
        const player = new Spotify.Player({
            name: 'Embedded Endian Device',
            getOAuthToken: cb => { cb(token); }
        });

        // Error handling
        player.addListener('initialization_error', ({ message }) => { console.error(message); });
        player.addListener('authentication_error', ({ message }) => { console.error(message); });
        player.addListener('account_error', ({ message }) => { console.error(message); });
        player.addListener('playback_error', ({ message }) => { console.error(message); });

        // Playback status updates
        player.addListener('player_state_changed', state => { console.log(state); });

        // Ready
        player.addListener('ready', ({ device_id }) => {
            console.log('Ready with Device ID', device_id);
        });

        // Not Ready
        player.addListener('not_ready', ({ device_id }) => {
            console.log('Device ID has gone offline', device_id);
        });

        // Connect to the player!
        player.connect();
        };
    </script>
    </body>
    </html>
    """

def spotifyPlayerSettings():
    app.run(debug=True, use_reloader=False)

if __name__ == "__main__":

    youtubeURL = "https://youtu.be/qQWAicHiVhk"

    # Set the alarm time
    alarmTime = "05:25 PM"

    alarmProcess = Process(target=setAlarm, args=(alarmTime, youtubeURL))
    alarmProcess.start()
    app.run(debug=True, use_reloader=False)
    alarmProcess.join()