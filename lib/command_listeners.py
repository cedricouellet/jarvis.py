import wikipedia
from typing import Callable, List
from lib import speech, user_input, media, greet, location, apis


__WIKIPEDIA = 'wikipedia'
__GOOGLE = 'google'
__YOUTUBE = 'youtube'
__WEATHER = 'weather'
__ADVICE = 'advice'
__COOL = 'cool'
__FCK_YOU = 'f*** you'
__DIE = 'die'

__PAUSE_OPTIONS = [
    'stop',
    'wait',
    'go away',
    'take a break'
]

__RESUME_OPTIONS = [
    'resume',
    'continue',
    'start',
    'jarvis'
]

__listeners = []


def add_listener(fct_listener: Callable):
    """
    Add a listener to the bot.

    :param fct_listener: The listener function to add.
    """
    if fct_listener not in __listeners:
        __listeners.append(fct_listener)


def get_listeners() -> List[Callable]:
    """
    Get all added listeners.
    :return: The listeners that were added.
    """
    return __listeners


def on_fck_you(listen_text: str) -> None:
    """
    Listen for the "f*** you" command.

    :param listen_text: The input text.
    """
    if __FCK_YOU in listen_text:
        speech.speak('Well fuck you too, sir.')


def on_cool(listen_text: str) -> None:
    """
    Listen for the cool command.

    :param listen_text: The input text.
    """
    if __COOL == listen_text:
        speech.speak('I know right?')


def on_pause(listen_text: str) -> None:
    """
    Listen for a command asking to pause the bot's listen mode.
    If enabled, the bot will stop responding to input until a resume command is spoken.

    :param listen_text: The input text
    """
    pause = False
    for pause_opt in __PAUSE_OPTIONS:
        if pause_opt not in listen_text:
            continue
        pause = True
        speech.speak('I will take a break. Let me know when you need me.')
        while pause is True:
            try:
                listen_text = user_input.process_speech(state_opening=False).lower()
                for resume_opt in __RESUME_OPTIONS:
                    if resume_opt in listen_text:
                        speech.speak('I am back. What can I do for you, sir?')
                        pause = False
            except:  # noqa
                pass


def on_weather(listen_text: str) -> None:
    """
    Listen for the Weather command

    :param listen_text: The input text
    """
    if __WEATHER in listen_text:
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
    if __ADVICE in listen_text:
        advice = apis.get_random_advice()
        speech.speak(f"Here is a piece of advice, sir. {advice}")


def on_google(listen_text: str) -> None:
    """
    Listen for the Google command

    :param listen_text: The input text
    """
    if __GOOGLE in listen_text:
        listen_text = __ask_search(__GOOGLE)
        media.search_google(listen_text)


def on_youtube(listen_text: str) -> None:
    """
    Listen for the YouTube command

    :param listen_text: The input text
    """
    if __YOUTUBE in listen_text:
        listen_text = __ask_search(__YOUTUBE)
        media.search_youtube(listen_text)


def on_die(listen_text: str) -> None:
    """
    Listen for the Die command

    :param listen_text: The input text
    """
    if __DIE in listen_text:
        speech.speak("I will now die.")
        greet.exit_bot()


def on_wikipedia(listen_text: str) -> None:
    """
    Listen for the Wikipedia command

    :param listen_text: The input text
    """
    if __WIKIPEDIA in listen_text:
        listen_text = __ask_search(__WIKIPEDIA)
        try:
            result = media.search_wikipedia(listen_text)
            speech.speak(result)
        except wikipedia.DisambiguationError as err:
            speech.speak(f'Sir, {listen_text} may refer to a few options. Do you want to hear them?')
            yes_or_no = user_input.process_speech().lower()
            if 'yes' in yes_or_no:
                i = 0
                for option in err.options:
                    speech.speak(f'Option number {i+1}: {option}')
                    i += 1
                speech.speak('Which option do you want, sir?')
                option = int(user_input.process_speech().lower())
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
    return user_input.process_speech().lower()
