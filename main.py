import pyttsx3
import speech_recognition as sr
import webbrowser as wb
import subprocess
import os
import pyautogui
from Features.custom_voice import speak
from time import sleep
from facedetection import load_face_data, detect_faces  # Import face detection

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
voicespeed = 170
engine.setProperty('rate', voicespeed)

# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()

# def takeCommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 1
#         r.energy_threshold = 300
#         audio = r.listen(source)
#
#     try:
#         print("Recognising...")
#         query = r.recognize_google(audio, language='en-in')
#         print(f"You said: {query}\n")
#     except Exception as e:
#         print("Say that again")
#         return "---"
#     return query

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        r.adjust_for_ambient_noise(source, duration=1)
        r.energy_threshold = 100
        print(f"Energy threshold set to: {r.energy_threshold}")
        print("Listening...")
        try:
            audio = r.listen(source, timeout=10, phrase_time_limit=10)
            print("Recognising...")
            query = r.recognize_google(audio, language='en-in')
            print(f"You said: {query}\n")
        except sr.UnknownValueError:
            print("Could not understand the audio.")
            return "---"
        except sr.RequestError as e:
            print(f"Google API error: {e}")
            return "---"
        except Exception as e:
            print(f"Error: {e}")
            return "---"
        return query


# if __name__ == "__main__":
#     while True:
#         query = takeCommand().lower()
#         print(query)
#
#         if "hello" in query:
#             from wishme import wishme
#             wishme()
if __name__ == "__main__":
    # print("Detecting face...")
    #
    # face_detected = detect_faces()  # Now only allows "Kaze"
    # if face_detected:
    #     print("Welcome, Kaze!")
    #     from wishme import wishme
    #     wishme()
    print("Welcome, Kaze!")
    # from wishme import wishme
    # wishme()
    while True:
            query = takeCommand().lower()
            if "go to sleep" in query:
                speak("Ok sir, You can call me anytime")
                break

            elif "hi" in query:
                speak("Hello sir, how are you")

            elif "I am fine" in query:
                speak("Good to hear that sir")

            elif "thank you" in query:
                speak("It's my pleasure sir")

            elif "good morning" in query:
                from wishme import wishme
                wishme()

            elif "Chrome" in query:
                from searchnew import openChrome
                openChrome(query)


            elif "open" in query:
                from Dictapp import openweb
                openweb(query)
                if "notepad" in query:
                    from type import type_in_notepad
                    type_in_notepad()


            elif "close" in query:
                from Dictapp import closeweb
                closeweb(query)

            elif "google" in query:
                from search import searchGoogle
                searchGoogle(query)

            # elif "youtube" in query:
            #     from search import searchYoutube
            #     searchYoutube(query)

            # elif "wikipedia" in query:
            #     from search import searchWikipedia
            #     searchWikipedia(query)

                # elif "temperature" or "weather" in query:
                #     from search import searchTemperature
                #     searchTemperature(query)

            elif "time" in query:
                from date_time import speak_current_time
                speak_current_time(query)

            elif "date" in query:
                from date_time import date
                date(query)

                # elif "joke" in query:
                #     speak(pyjokes.get_jokes())
                #     #print(pyjokes)

                # Logout/Shutdown/Restart
            elif "do logout" in query:
                speak('logging out in 5 second')
                sleep(5)
                os.system("shutdown - l")

            elif "shutdown" in query:
                speak('shutting down in 5 second')
                sleep(5)
                os.system("shutdown /s /t 1")

            elif "restart" in query:
                speak('restarting in 5 second')
                sleep(5)
                os.system("shutdown /r /t 1")

            elif "menu" in query:
                pyautogui.hotkey('winleft', 'x')

            elif "open task manager" in query:
                pyautogui.hotkey('ctrl', 'shift', 'esc')

            elif "take screenshot" in query:
                pyautogui.hotkey('winleft', 'prtscr')
                speak("done")

            elif "take ss" in query:
                pyautogui.hotkey('winleft', 'shift', 's')

            elif "open setting" in query:
                pyautogui.hotkey('winleft', 'i')


# else:
#         print("Access Denied!")