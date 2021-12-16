import pyttsx3

engine = pyttsx3.init('sapi5')


def init():
    """
    Initialize the speech engine.
    Must be called before all other methods in the module.
    """
    engine.setProperty('rate', 200)
    engine.setProperty('volume', 1.0)

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Set male voice


def speak(text):
    """
    Say a sentence (text to speech)
    :param text: The text to speak
    """

    engine.say(text)
    engine.runAndWait()

