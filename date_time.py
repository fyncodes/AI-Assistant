import datetime
import pyttsx3
import speech_recognition as sr

from Features.custom_voice import speak


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)
    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "---"
    return query


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
voicespeed = 170
engine.setProperty('rate', voicespeed)

query = takeCommand().lower()


def speak_current_time(query):
    """Speak the current time if 'time' is in the query."""
    if "time" in query:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(current_time)
        print(current_time)


def date(query):
    if "date" in query:
        day = int(datetime.datetime.now().day)
        month = int(datetime.datetime.now().month)
        year = int(datetime.datetime.now().year)
        speak("The current date is")
        print(day, month, year)
        date_a = (day, month, year)
        speak(date_a)
