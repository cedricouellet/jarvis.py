from lib import greet, speech, user_input, command_listeners as cl

cl.add_listener(cl.on_pause)
cl.add_listener(cl.on_die)
cl.add_listener(cl.on_google)
cl.add_listener(cl.on_youtube)
cl.add_listener(cl.on_wikipedia)
cl.add_listener(cl.on_weather)
cl.add_listener(cl.on_advice)
cl.add_listener(cl.on_cool)
cl.add_listener(cl.on_fck_you)


def main() -> None:
    """Entry point function"""

    # IMPORTANT
    # We must initialize the speech engine before everything else
    speech.init()

    greet.start_bot()

    # Start the listening event loop
    listen()


def listen():
    """
    1. Initialize listeners.
    2. Listen to for user input
    3. Try to parse the input, depending on the listeners that are declared.
    """
    try:
        while True:
            query = user_input.process_speech(state_opening=False).lower()
            print(query)

            for init_listener in cl.get_listeners():
                init_listener(query)

    except KeyboardInterrupt:
        greet.exit_bot()
    except Exception:  # noqa
        speech.speak("I could not understand. Could you repeat that, sir?")
        listen()


if __name__ == '__main__':
    main()
