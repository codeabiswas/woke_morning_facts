import datetime
import time
import requests
import random
import vlc
import pafy
import yaml

# Author:       Andrei Biswas
# GitHub:       codeabiswas
# Email:        petitendian@gmail.com

# Created on:   Tuesday, July 18, 2019
# Modified on:  Wednesday, August 7, 2019

"""
    This class is for the YouTube VLC player
"""
class vlc_player:

    """
        This method initializes the VLC media player object
    """
    def __init__(self, youtubeURL):
        
        # If it is a playlist, get a random video from the playlist
        try:
            playlist = pafy.get_playlist(youtubeURL)
            randomIndex = random.randint(0, len(playlist['items']))
            best = playlist['items'][randomIndex]['pafy'].getbestaudio()
        except:
            # Get the video object
            video = pafy.new(youtubeURL)
            # Get the best audio from the youtube URL
            best = video.getbestaudio()
        
        # Fetch a VLC Instance
        instance = vlc.Instance()
        # Create a new VLC player
        self.player = instance.media_player_new()
        # Get the media object
        self.media = instance.media_new(best.url)
        # Get the media objects MRL
        self.media.get_mrl()
        # Set the player to play the media object
        self.player.set_media(self.media)
    
    """
        This method plays the YouTube video
    """
    def play(self):
        
        # Set media player volume to 100
        self.player.audio_set_volume(100)
        # Play the media
        self.player.play()
    
    """
        This method stops the YouTube video by fading out. 
    """
    def stop(self):
        
        # Max volume as a counter
        volumeCounter = 100

        # Until the player is not mute, bring down the volume every 0.25 seconds
        while volumeCounter != 0:
            self.player.audio_set_volume(volumeCounter)
            volumeCounter -= 1
            time.sleep(0.25)

        # Bring back the volume to 100
        self.player.audio_set_volume(100)
        # Stop the media
        self.player.stop()
        
"""
    Fetch settings from the config.yml file
"""
def get_settings():

    # Load all the data into the config variable and return it in a list format
    with open("config.yml", 'r') as ymlfile:
        config = yaml.load(ymlfile, Loader=yaml.SafeLoader)

    # Check if the user has filled out the appropriate data
    if config['youtube_url'] == 'your-youtube-url-here':
        print("Please add a YouTube playlist/video link.")
        return []

    if config['alarm_time'] == 'your-alarm-time-here':
        print("Please add an alarm time.")
        return []

    return [config['youtube_url'], config['snooze_time'], config['alarm_time']]
    
"""
    Sets the alarm and prints a fun fact when the alarm "rings"
"""
def set_alarm(configData):

    # YouTube URL
    youtubeURL = configData[0]
    
    # Snooze Time
    snoozeTime = configData[1]
    
    # Alarm Time
    alarmTime = configData[2]
    
    # Set the alarm time to exact :00 seconds
    alarmTime = alarmTime[0:5] + ":00"

    # Save the default alarm time
    defaultAlarmTime = alarmTime
    
    # Get the current time
    currTime = time.strftime("%H:%M:%S")

    someAlarm = vlc_player(youtubeURL)

    # Run forever
    while True:
        # Until it is time for the alarm, just keep printing the current time
        if (currTime != alarmTime):
            time.sleep(1)

        else:
            
            # Play the alarm
            someAlarm.play()
            # Ask user for stop alarm or snooze
            typeOfAlarm = input("Snooze or Stop (Press s for stop, and anything else for snooze)?  ")

            # If the alarm is to be stopped, set the default alarm time
            if typeOfAlarm == 's':
                print(fetch_fact())
                alarmTime = defaultAlarmTime
                print("New Alarm Time: {}".format(alarmTime))
                
            # Otherwise, delay alarm by snooze time set in config file
            else:
                alarmTime = datetime.datetime.strptime(time.strftime("%H:%M:%S"), '%H:%M:%S') + datetime.timedelta(days=0, seconds=(snoozeTime*60))
                alarmTime = alarmTime.strftime("%H:%M:%S")
                print("New Alarm Time: {}".format(alarmTime))
            
            # "Nicely" stop the alarm
            someAlarm.stop()
                
        # Update the time            
        currTime = time.strftime("%H:%M:%S")
        print("Current Time: ", currTime)
            
"""
    Fetch a fact given the date
"""
def fetch_fact():

    # Fetch today's day and month
    todayDay = datetime.date.today().strftime("%d")
    todayMonth = datetime.date.today().strftime("%m")

    # Format the day and month
    if todayDay[0] == '0':
        todayDay = todayDay[1]

    if todayMonth[0] == '0':
        todayMonth = todayMonth[1]

    # API-Endpoint
    url = "http://numbersapi.com/" + todayMonth + "/" + todayDay + "/date?json"

    # Get the response object
    factResponse = requests.get(url=url)

    # Fetch the fact from the JSON objectDDidDidDidid
    fact = factResponse.json()["text"]

    return fact

"""
    This method defines what this program mainly does
"""
def main():

    # Fetch the settings containing all the information
    configData = get_settings()

    # If an error has occured (indicated by empty list), just exit the program
    if len(configData) == 0:
        return

    #set_alarm(alarmTime, snoozeTime, youtubeURL)
    set_alarm(configData)

if __name__ == "__main__":
    # Run the main program
    main()