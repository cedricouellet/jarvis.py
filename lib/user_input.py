import speech_recognition as sr
from random import choice

from lib.speech import speak
from lib.utils import opening_text
from lib import greet

exit_messages = [
    'stop',
    'exit'
]


def take_user_input() -> str:
    """
    1. Takes user input.
    2. Processes the input.
    3. Converts the input into text.

    :return: The input converted into text, or "None"
    """

    # Construct the recognition object
    r = sr.Recognizer()
    r.pause_threshold = 1

    # Listen for audio
    audio = listen(r)

    # Attempt to process the audio
    try:
        print('Processing audio...')
        query = r.recognize_google(audio, language='en-us')

        # If the user asks to exit, stop listening for input
        # (exit the bot)
        for exit_msg in exit_messages:
            if exit_msg in query:
                greet.stop()

        speak(choice(opening_text))  # Say a random opening

    except Exception:  # noqa
        speak('Sorry, I could not understand. Could you please repeat what you said?')
        query = 'None'
    return query


def listen(recognizer: sr.Recognizer) -> sr.AudioData:
    """
    Listen for speech

    :param recognizer: The object used to recognize audio
    :return: The audio data that was read.
    """
    with sr.Microphone() as source:
        print('Listening for audio...')
        audio = recognizer.listen(source)
    return audio
