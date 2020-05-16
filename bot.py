import requests

from http import HTTPStatus

from config import TelegramAPIConfig
from logger import logger


def get_updates_json() -> dict:
    """Get updates from bot API."""
    try:
        response = requests.get(TelegramAPIConfig.UPDATES_URL, timeout=TelegramAPIConfig.TIMEOUT_SECONDS)
    except (ConnectionError, requests.exceptions.ConnectTimeout) as http_ex:
        logger.error(f"Connection to bot API failed: {http_ex}.")
        return {}

    if response.status_code != HTTPStatus.OK:
        logger.error(f"Telegram API code error. Updates request failed with {response.status_code} code.")
        return {}

    if not response.json().get("ok"):
        logger.error(f"Telegram API response error. Updates request OK parameter is not true.")
        return {}

    return response.json()


def last_update(data):
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]