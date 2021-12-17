import speech_recognition as sr
from random import choice

from lib.speech import speak
from lib.utils import opening_text
from lib import greet

exit_messages = [
    'exit',
    'goodbye'
]


def take_user_input(state_opening: bool = True) -> str:
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
    audio = __listen(r)

    # Attempt to process the audio
    try:
        print('Processing audio...')
        query = r.recognize_google(audio, language='en-us')

        # If the user asks to exit, stop listening for input
        # (exit the bot)
        for exit_msg in exit_messages:
            if exit_msg == query:
                greet.stop()

        if state_opening:
            speak(choice(opening_text))  # Say a random opening
        return query

    except Exception as e:  # noqa
        raise e


def __listen(recognizer: sr.Recognizer) -> sr.AudioData:
    """
    Listen for speech

    :param recognizer: The object used to recognize audio
    :return: The audio data that was read.
    """
    with sr.Microphone() as source:
        print('Listening for audio...')
        audio = recognizer.listen(source)
    return audio
