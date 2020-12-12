"""Telegram bot configuration."""


# Token to access the HTTP API
BOT_TOKEN = '912794474:AAGnEfiHOj396xJ7hMduva16Dv7wbPysuvE'

REQUEST_TIMEOUT_SECONDS = 3

# Proxy for those old times, when Telegram was blocked.
PROXY = {
    'proxy_url': 'socks5://t3.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python',
    }
}

GOOGLE_SEARCH_PHRASE = 'COVID-19'
GOOGLE_SEARCH_PERIOD = '1d'
GOOGLE_SEARCH_LIMIT = 3
