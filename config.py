"""Telegram bot configuration.

BOT_TOKEN - token to access the HTTP API
TelegramAPIConfig.API_URL - Telegram API url
TelegramAPIConfig.UPDATES_URL - bot updates (24 hour period)
"""

BOT_TOKEN = ''


class TelegramAPIConfig:

    API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"
    TIMEOUT_SECONDS = 3
    UPDATES_URL = f"{API_URL}/getUpdates"
