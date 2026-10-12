import pyttsx3
import datetime

from Features.custom_voice import speak

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
voicespeed = 170
engine.setProperty('rate', voicespeed)


def wishme():
    hour = datetime.datetime.now().hour
    if 6 <= hour <= 12:
        speak('Good morning')
    elif 12 <= hour <= 18:
        speak('Good afternoon')
    elif 18 <= hour <= 24:
        speak('Good evening')
    else:
        speak('Good to see you again')

    speak("I'm here at your service!")
