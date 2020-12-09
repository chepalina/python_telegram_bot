"""WebSite parser https://xn--80aesfpebagmfblc0a.xn--p1ai/."""

from html.parser import HTMLParser
from typing import List
import requests

from config import REQUEST_TIMEOUT_SECONDS
from logger import logger


DAILY_STAT_PHRASE = 'Выявлено случаевза последние сутки'
WEB_SITE_URL = "https://xn--80aesfpebagmfblc0a.xn--p1ai/"


def get_statistic():
    response = requests.get(WEB_SITE_URL, timeout=REQUEST_TIMEOUT_SECONDS)

    parser = _StopCovidHTMLParser()
    parser.feed(response.text)
    daily_stat = parser.data.get(DAILY_STAT_PHRASE)
    if daily_stat is None:
        logger.error("Daily statistic was not found.")
        logger.debug(f"Info that was managed to parse: {parser.data}")
        return "I can't get statistic. I'm really ashamed :( Hope COVID pandemic is over!"

    return f"The number of cases in the last day: {daily_stat}"


class _StopCovidHTMLParser(HTMLParser):
    """Parser of https://xn--80aesfpebagmfblc0a.xn--p1ai/ site."""
    data = {}

    _DIV_TAG = 'div'
    _VALUE = 'value'
    _LABEL = 'label'

    _label_flg = False
    _label_str = ''

    _value_flg = False
    _value_str = ''

    def handle_starttag(self, tag: str, attrs: List[tuple]):
        """Handle label and value tags."""

        for attr in attrs:
            _, value = attr

            if value is None:
                return
            elif self._VALUE in value:
                self._value_flg = True
            elif self._LABEL in value:
                self._label_flg = True

    def handle_endtag(self, tag: str):
        """Add collected data to dict."""

        if tag == self._DIV_TAG:

            if self._label_flg:
                # We know, that value goes before label
                self.data[self._label_str] = self._value_str
                self._label_flg = False
                self._label_str = ''
                self._value_flg = False
                self._value_str = ''

    def handle_data(self, data: str):
        """Collect data from web page."""

        if self._label_flg:
            self._label_str += data.strip()
        elif self._value_flg:
            self._value_str += data.strip()

    def error(self, message: Exception):
        logger.error(f"Parsing error: {message}")
