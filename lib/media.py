import pywhatkit as kit
import wikipedia
import wikipedia.exceptions


def search_google(query: str) -> None:
    """
    Search something on Google.
    Opens a tab in the default browser.

    :param query: The query to search on google
    """
    kit.search(query)


def search_youtube(query: str) -> None:
    """
    Search something on YouTube.
    Opens a tab in the default browser.

    :param query: The query to search on YouTube
    """
    kit.playonyt(query)


def search_wikipedia(query: str) -> str:
    """
    Search something on Wikipedia.
    :param query: The query to search on Wikipedia
    :return: The results of the search
    """
    try:
        return wikipedia.summary(query, sentences=2, auto_suggest=True)
    except wikipedia.exceptions.DisambiguationError as err:
        raise err
