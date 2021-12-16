from decouple import config
from lib import greet, speech, user_input, listeners

USERNAME = config('USER')
BOTNAME = config('BOTNAME')


def main() -> None:
    """Entry point function"""
    speech.init()
    greet.greet_user(BOTNAME, USERNAME)

    try:
        while True:
            query = user_input.take_user_input().lower()

            listeners.on_die(query)
            listeners.on_google(query)
            listeners.on_youtube(query)
            listeners.on_wikipedia(query)
    except KeyboardInterrupt:
        greet.stop()


if __name__ == '__main__':
    main()

