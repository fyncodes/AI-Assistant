import os
import pyautogui
import pyttsx3
import webbrowser as wb

from Features.custom_voice import speak
from time import sleep

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
voicespeed = 170
engine.setProperty('rate', voicespeed)

# dictapp = {
#     "commandprompt": "cmd",
#     "paint": "mspaint",
#     "word": "winword",
#     "excel": "excel",
#     "notepad": "notepad",
#     }

dictapp = {
    "command prompt": "cmd",
    "paint": "mspaint",
    "word": "winword",
    "excel": "excel",
    "notepad": "notepad",
    "file explorer": "explorer",
    "microsoft store": "ms-windows-store:",
    "calculator": "calc",
    "task manager": "taskmgr",
    "control panel": "control",
    "settings": "ms-settings:",
    "powershell": "powershell",
    "snipping tool": "snippingtool",
    "media player": "wmplayer",
    "outlook": "outlook",
    "Chrome": "chrome",
    "firefox": "firefox",
    "edge": "msedge",
    "vlc player": "vlc",
    "zoom": "zoom",
    "spotify": "spotify",
    "discord": "discord",
    "teams": "teams"
}

def openweb(query):
    if any(domain in query for domain in [".com", ".org", ".co.in"]):
        query = query.replace("open", "").replace("AOI", "").replace("launch", "").strip()
        wb.open(f"https://{query}")
        speak("Website is launched")
    else:
        for app in dictapp:
            if app in query:
                os.system(f"start {dictapp[app]}")
                speak(f"The {dictapp[app]} is launched")
                break

def closeweb(query):
    if "1 tab" in query or "one tab" in query:
        pyautogui.hotkey("ctrl", "w")
        speak("Tab is closed")
    elif "2 tabs" in query or "two tabs" in query:
        for _ in range(2):
            pyautogui.hotkey("ctrl", "w")
            sleep(0.5)
        speak("2 Tabs are closed")
    elif "3 tabs" in query or "three tabs" in query:
        for _ in range(3):
            pyautogui.hotkey("ctrl", "w")
            sleep(0.5)
        speak("3 Tabs are closed")

    else:
        for app in dictapp:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")
                speak(f"{dictapp[app]} is closed")
                break
