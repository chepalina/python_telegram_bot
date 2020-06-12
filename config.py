"""Telegram bot configuration.

BOT_TOKEN - token to access the HTTP API
TelegramAPIConfig.API_URL - Telegram API url
TelegramAPIConfig.UPDATES_URL - bot updates (24 hour period)
"""

BOT_TOKEN = ''

REQUEST_TIMEOUT_SECONDS = 3

REQUEST_KWARGS = {
    'proxy_url': 'socks5://t3.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python',
    }
}

BOT_START_TEXT = "Hi! I'm bot, who knows a few statistic about COVID-19 in Russia." \
                 "\nUse commands: \n/get_stat - to get current statistic. " \
                 "\n/get_dates - get dates when boarders will be opened."
