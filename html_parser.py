from html.parser import HTMLParser

from logger import logger


class StopCovidHTMLParser(HTMLParser):
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
