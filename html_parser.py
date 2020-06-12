"""
TODO: Type hints.
"""
import requests
from html.parser import HTMLParser

from logger import logger
from config import REQUEST_TIMEOUT_SECONDS
from html_table_parser import HTMLTableParser


__all__ = ["get_daily_stat_message"]

DAILY_STAT_PHRASE = 'Выявлено заболевшихза последние сутки'
WEB_SITE_URL = "https://xn--80aesfpebagmfblc0a.xn--p1ai/"


def get_daily_stat_message():
    response = requests.get(WEB_SITE_URL, timeout=REQUEST_TIMEOUT_SECONDS)

    parser = _StopCovidHTMLParser()
    parser.feed(response.text)
    daily_stat = parser.DATA_DICT.get(DAILY_STAT_PHRASE)
    if daily_stat is None:
        logger.error("Daily statistic was not found.")
        logger.debug(f"Info that was managed to parse: {parser.DATA_DICT}")
        return "I can't get statistic. I'm really ashamed :( Hope COVID pandemic is over!"

    return f"The number of cases in the last day: {daily_stat}"


class _StopCovidHTMLParser(HTMLParser):
    """Parser of https://xn--80aesfpebagmfblc0a.xn--p1ai/ site."""

    LABEL_FLG = False
    LABEL_STRING = ''

    VALUE_FLG = False
    VALUE_STRING = ''

    DATA_DICT = {}

    def handle_starttag(self, tag, attrs):
        """Handle label and value tags."""

        for attr in attrs:
            _, value = attr

            if value is None:
                return
            elif 'value' in value:
                self.VALUE_FLG = True
            elif 'label' in value:
                self.LABEL_FLG = True

    def handle_endtag(self, tag):
        """Add collected data to dict."""

        if tag == 'div':

            if self.LABEL_FLG:
                # We know, that value goes before label
                self.DATA_DICT[self.LABEL_STRING] = self.VALUE_STRING
                self.LABEL_FLG = False
                self.LABEL_STRING = ''
                self.VALUE_FLG = False
                self.VALUE_STRING = ''

    def handle_data(self, data):
        """Collect data from web page."""

        if self.LABEL_FLG:
            self.LABEL_STRING += data.strip()
        elif self.VALUE_FLG:
            self.VALUE_STRING += data.strip()

    def error(self, message):
        logger.error(f"Parsing error: {message}")


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

