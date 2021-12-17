import wikipedia

from lib import speech, user_input, media, greet, location, apis

WIKIPEDIA = 'wikipedia'
GOOGLE = 'google'
YOUTUBE = 'youtube'
WEATHER = 'weather'
ADVICE = 'advice'


pause_options = [
    'stop',
    'wait',
    'go away',
    'take a break'
]

resume_options = [
    'resume',
    'continue',
    'start',
    'jarvis'
]


def on_pause(listen_text: str) -> None:
    """
    Listen for a command asking to pause the bot's listen mode.
    If enabled, the bot will stop responding to input until a resume command is spoken.

    :param listen_text: The input text
    """
    for pause in pause_options:
        if pause not in listen_text:
            continue
        speech.speak('I will take a break. Let me know when you need me.')
        while True:
            try:
                listen_text = user_input.take_user_input(state_opening=False).lower()
                for resume in resume_options:
                    if resume not in listen_text:
                        continue
                    speech.speak('I am back. What can I do for you, sir?')
                    break
                break
            except:  # noqa
                pass


def on_weather(listen_text: str) -> None:
    """
    Listen for the Weather command

    :param listen_text: The input text
    """
    if WEATHER in listen_text:
        speech.speak("Getting the weather report for you city, sir.")
        current_city = location.get_city()
        weather, temp, feels_like = apis.get_weather(current_city)

        speech.speak(f"Weather for {current_city}:")
        speech.speak(f"The current conditions include {weather}. The current temperature is {temp}, "
                     f"but it feels like {feels_like}")


def on_advice(listen_text: str) -> None:
    """
    Listen for the Advice command

    :param listen_text: The input text
    """
    if ADVICE in listen_text:
        advice = apis.get_random_advice()
        speech.speak(f"Here is a piece of advice, sir. {advice}")


def on_google(listen_text: str) -> None:
    """
    Listen for the Google command

    :param listen_text: The input text
    """
    if GOOGLE in listen_text:
        listen_text = __ask_search(GOOGLE)
        media.search_google(listen_text)


def on_youtube(listen_text: str) -> None:
    """
    Listen for the YouTube command

    :param listen_text: The input text
    """
    if YOUTUBE in listen_text:
        listen_text = __ask_search(YOUTUBE)
        media.search_youtube(listen_text)


def on_die(listen_text: str) -> None:
    """
    Listen for the Die command

    :param listen_text: The input text
    """
    if 'die' in listen_text:
        speech.speak("I will now die.")
        greet.stop()


def on_wikipedia(listen_text: str) -> None:
    """
    Listen for the Wikipedia command

    :param listen_text: The input text
    """
    if WIKIPEDIA in listen_text:
        listen_text = __ask_search(WIKIPEDIA)
        try:
            result = media.search_wikipedia(listen_text)
            speech.speak(result)
        except wikipedia.DisambiguationError as err:
            speech.speak(f'Sir, {listen_text} may refer to a few options. Do you want to hear them?')
            yes_or_no = user_input.take_user_input().lower()
            if 'yes' in yes_or_no:
                i = 0
                for option in err.options:
                    speech.speak(f'Option number {i+1}: {option}')
                    i += 1
                speech.speak('Which option do you want, sir?')
                option = int(user_input.take_user_input().lower())
                result = media.search_wikipedia(err.options[option-1])
                speech.speak(result)
                speech.speak('Okay sir, I am done.')
            else:
                speech.speak('Okay sir, Nevermind then.')


def __ask_search(platform: str) -> str:
    """
    Ask to specify something to search depending on the platform.

    :param platform: The platform on which to search
    :return: The input to search
    """
    speech.speak(f'What do you want to search on {platform}, sir?')
    return user_input.take_user_input().lower()
