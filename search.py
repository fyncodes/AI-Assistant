import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser as wb
import requests

from Features.custom_voice import speak
from bs4 import BeautifulSoup

chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"

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

# def openChrome(query):
#     if "open Chrome" in query:
#         url = "chrome://newtab"
#         wb.get(chrome_path).open(url)
#         speak("Opening Chrome")

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScarp
        query = query.replace("Aoi", "")
        query = query.replace("search", "")
        query = query.replace("google search", "")
        query = query.replace("google", "")
        speak("This what I found on Google")

        try:
            pywhatkit.search(query)
            result = googleScarp.summary(query, 1)
            speak(result)

        except:
            speak("Not recognized")

def searchYoutube(query):
    if "youtube" in query:
        speak("This is what I found in Youtube  ")
        query = query.replace("Aoi", "")
        query = query.replace("youtube search", "")
        query = query.replace("youtube", "")
        web = "https://www.youtube.com/results?search_query=" + query
        wb.open(web)
        pywhatkit.playonyt(query)


def searchWikipedia(query):
    if "wikipedia" in query:
        speak("This is what I found in wikipedia  ")
        query = query.replace("Aoi", "")
        query = query.replace("wikipedia search", "")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("This information is in wikipedia")
        print(results)
        speak(results)


def searchTemperature(query):
    if "temperature" or "weather" in query:
        #query = query.replace("current", "")
        search = "temperature"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        temp = data.find("div", class_ = "BNeawe").text
        speak(f"The current {search} is {temp}")

