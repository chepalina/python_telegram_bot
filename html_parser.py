"""
TODO: Type hints.
"""
import requests

from config import REQUEST_TIMEOUT_SECONDS
from html_table_parser import HTMLTableParser


__all__ = []

VISACON_SITE = 'https://visacom.ru/tablitsa-predpolozhitelnogo-otkrytiya-granits'

response = requests.get(VISACON_SITE, timeout=REQUEST_TIMEOUT_SECONDS)


def get_open_countries():
    parser = HTMLTableParser(data_separator=', ')
    parser.feed(response.text)
    table = parser.tables[0]
    open_date = 'I know when countries open boarders! \n\n'
    for date, countries in table:
        open_date += f'{date}: {countries} \n'
    return open_date
