import wikipedia

from lib import speech, user_input, media, greet

WIKIPEDIA = 'wikipedia'
GOOGLE = 'google'
YOUTUBE = 'youtube'


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
