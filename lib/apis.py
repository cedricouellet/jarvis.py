from decouple import config
import requests


OPENWEATHER_API_KEY = config('OPENWEATHER_API_KEY')


def get_weather(city: str):
    """
    Get the weather for a city.

    :param city: The city for which to get the weather.
    :return: The weather report for the city.
    """
    res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}"
                       f"&units=metric&appid={OPENWEATHER_API_KEY}").json()

    weather = res["weather"][0]["main"]
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]

    return weather, f"{temperature}℃", f"{feels_like}℃"


def get_random_advice() -> str:
    """
    Get a random piece of advice.

    :return: The random piece of advice.
    """
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']
