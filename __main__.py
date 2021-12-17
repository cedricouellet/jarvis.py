from decouple import config
from lib import greet, speech, user_input, listeners


def main() -> None:
    """Entry point function"""
    speech.init()
    greet.greet_user()
    listen()


def listen():
    try:
        while True:
            query = user_input.take_user_input(False).lower()
            print(query)

            if 'cool' == query:
                speech.speak('I know right?')

            if 'f*** you' in query:
                speech.speak('Well fuck you too, sir.')

            listeners.on_pause(query)
            listeners.on_die(query)
            listeners.on_google(query)
            listeners.on_youtube(query)
            listeners.on_wikipedia(query)
            listeners.on_weather(query)
            listeners.on_advice(query)
    except KeyboardInterrupt:
        greet.stop()
    except Exception:  # noqa
        speech.speak("I could not understand. Could you repeat that, sir?")
        listen()


if __name__ == '__main__':
    main()
