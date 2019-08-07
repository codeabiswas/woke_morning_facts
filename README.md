# woke_morning_facts

Wake up to audio from a YouTube playlist video or just a YouTube video link. When you stop the alarm, get rewarded with a fun fact about that date.

---

## Usage and Example

*Input:* 

```python main.py```

*Output:* 
```python
Current Time:  13:48:06
Current Time:  13:48:07
Current Time:  13:48:08
Current Time:  13:48:09
Current Time:  13:48:10
...
Current Time:  13:48:55
Current Time:  13:48:56
Current Time:  13:48:57
Current Time:  13:48:58
Current Time:  13:48:59
Current Time:  13:49:00
Snooze or Stop (Press s for stop, and anything else for snooze)?  s
August 7th is the day in 1985 that Takao Doi, Mamoru Mohri and Chiaki Mukai are chosen to be Japan's first astronauts.

```

---

## Installation

__Note:__ *This has only been tried and tested on Debian. This installation guide may not work exactly the same way on other operating systems.*

1. Install everything on the ```requirements.txt``` file.
```pip install -r requirements.txt```

2. Update the ```config.yml``` file with:
    1. A YouTube playlist or video link
    2. Update the snooze time, which is in minutes (Default is 15 minutes) 
    3. The alarm time in military, HH:MM format (this is the time the alarm will start everyday)
    
You are set!

---

## Acknowledgements
* This project is powered by [python-vlc](https://pypi.org/project/python-vlc/) and the [Numbers API](http://numbersapi.com/#42).

---

## Contributors
* Andrei Biswas: axb6972@rit.edu

---

## License
```woke_morning_facts``` is under the MIT license.