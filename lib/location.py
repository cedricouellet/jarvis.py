import requests


def get_city() -> str:
    """
    Find the city in which the user is in.

    :return: The city of the user
    """
    res = requests.get('https://geolocation-db.com/json').json()
    return res["city"]
