import pyautogui
from Features.custom_voice import speak
from main import takeCommand
from time import sleep

def type_in_notepad():
    speak("Do you want me to start typing?")
    confirmation = takeCommand().lower()
    if "yes" in confirmation or "start" in confirmation:
        speak("Okay, I'm listening. Say 'stop typing' to end.")
        sleep(2)  # Give you time to click on Notepad
        while True:
            typed_text = takeCommand().lower()
            if "stop typing" in typed_text:
                speak("Stopped typing.")
                break
            elif typed_text != "---":
                pyautogui.write(typed_text)
                pyautogui.press("enter")
