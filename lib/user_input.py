import speech_recognition as sr
from random import choice

from lib.speech import speak
from lib.utils import opening_text
from lib import greet

exit_messages = [
    'exit',
    'goodbye'
]


def process_speech(state_opening: bool = True) -> str:
    """
    1. Takes user input.
    2. Processes the input.
    3. Converts the input into text.

    :param state_opening: If the bot states a message stating that
        it is trying to process the request.
    :return: The input converted into text
    :raise Exception: If there was an error processing the input.
    """

    # Construct the recognition object
    r = sr.Recognizer()
    r.pause_threshold = 1

    # Listen for audio
    audio = __listen(r)

    # Attempt to process the audio
    try:
        print('-- STATUS: processing --')
        query = r.recognize_google(audio, language='en-us')

        # If the user asks to exit, stop listening for input
        # (exit the bot)
        for exit_msg in exit_messages:
            if exit_msg == query:
                greet.exit_bot()

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
        print('-- STATUS: listening --')
        audio = recognizer.listen(source)
    return audio
