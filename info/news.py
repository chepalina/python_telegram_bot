from GoogleNews import GoogleNews

from config import GOOGLE_SEARCH_LIMIT, GOOGLE_SEARCH_PERIOD, GOOGLE_SEARCH_PHRASE
from logger import logger


_ERROR_MESSAGE = 'Google search was failed. No links, no news.'


def get_last_news():
    """Get last news from google."""
    google_news = GoogleNews(period=GOOGLE_SEARCH_PERIOD)
    try:
        google_news.search(GOOGLE_SEARCH_PHRASE)
    except Exception as ex:
        logger.error(f'Google search was failed. {ex}.')
        return [_ERROR_MESSAGE]
    return google_news.get_links()[:GOOGLE_SEARCH_LIMIT]
