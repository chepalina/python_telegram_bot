import requests

from http import HTTPStatus

from config import TelegramAPIConfig
from logger import logger
from html_parser import StopCovidHTMLParser


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



DAILY_STAT_PHRASE = 'Выявлено заболевшихза последние сутки'


def get_info(url):
    response = requests.get(url, timeout=TelegramAPIConfig.TIMEOUT_SECONDS)

    parser = StopCovidHTMLParser()
    parser.feed(response.text)
    daily_stat = parser.DATA_DICT.get(DAILY_STAT_PHRASE)
    if daily_stat is None:
        logger.error("Daily statistic was not found.")
        logger.debug(f"Info that was managed to parse: {parser.DATA_DICT}")

    print(parser.DATA_DICT)
    return daily_stat


get_info("https://xn--80aesfpebagmfblc0a.xn--p1ai/")


def last_update(data):
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]