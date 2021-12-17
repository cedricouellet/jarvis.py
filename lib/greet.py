from decouple import config
from datetime import datetime
from lib.speech import speak


USERNAME = config('USER')
BOTNAME = config('BOTNAME')


def greet_user() -> None:
    """
    Greet a user (TTS).
    """

    hour = datetime.now().hour  # Get the current time

    greeting = ""

    if 6 <= hour < 12:  # If in morning
        greeting = f"Good morning {USERNAME}"
    elif 12 <= hour < 16:  # If in afternoon
        greeting = f"Good afternoon {USERNAME}"
    elif 16 <= hour < 19:  # If in evening
        greeting = f"Good evening {USERNAME}"

    speak(greeting)
    speak(f"I am {BOTNAME}. How may I assist you?")


def stop():
    hour = datetime.now().hour

    if 21 <= hour < 6:
        greeting = "Good night sir, take care!"
    else:
        greeting = "Have a good day, sir!"

    speak(greeting)
    exit(0)
