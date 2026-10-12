import pyautogui
import time
import webbrowser as wb
from Features.custom_voice import speak

chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"

def openChrome(query):
    if "chrome" in query:
        speak("Opening Chrome")
        wb.get(chrome_path).open("https://www.google.com")
        time.sleep(3)  # Wait for Chrome to load

        # Focus address/search bar
        pyautogui.hotkey("ctrl", "l")
        time.sleep(1)

        # Type search query
        speak("What should I search?")
        from main import takeCommand  # If you have central speech file
        search_query = takeCommand().lower()
        pyautogui.write(search_query)
        pyautogui.press("enter")
