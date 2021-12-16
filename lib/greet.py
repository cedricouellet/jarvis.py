from datetime import datetime
from lib.speech import speak


def greet_user(botname: str, user: str) -> None:
    """
    Greet a user (TTS).

    :param user: The user to greet
    :param botname: The name of the bot
    """

    hour = datetime.now().hour  # Get the current time

    greeting = ""

    if 6 <= hour < 12:  # If in morning
        greeting = f"Good morning {user}"
    elif 12 <= hour < 16:  # If in afternoon
        greeting = f"Good afternoon {user}"
    elif 16 <= hour < 19:  # If in evening
        greeting = f"Good evening {user}"

    speak(greeting)
    speak(f"I am {botname}. How may I assist you?")


def stop():
    hour = datetime.now().hour

    if 21 <= hour < 6:
        greeting = "Good night sir, take care!"
    else:
        greeting = "Have a good day, sir!"

    speak(greeting)
    exit(0)
