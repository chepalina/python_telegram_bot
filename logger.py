"""Logger configuration."""
import logging

_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
_LOGGER_NAME = 'bot'

logging.basicConfig(format=_FORMAT,
                    level=logging.INFO)

logger = logging.getLogger(_LOGGER_NAME)
logger.setLevel(logging.DEBUG)
