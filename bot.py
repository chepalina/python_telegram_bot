from telegram.ext import CommandHandler, Updater

from commands import start, get_statistic, get_last_news
from config import PROXY, BOT_TOKEN


def build_bot():
    """Create bot updater, add handlers."""
    bot_ = Updater(token=BOT_TOKEN, use_context=True, request_kwargs=PROXY)

    dispatcher = bot_.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    help_handler = CommandHandler('help', start)
    dispatcher.add_handler(help_handler)

    get_stat_handler = CommandHandler('statistic', get_statistic)
    dispatcher.add_handler(get_stat_handler)

    get_dates_handler = CommandHandler('news', get_last_news)
    dispatcher.add_handler(get_dates_handler)

    return bot_


if __name__ == '__main__':

    bot = build_bot()
    bot.start_polling()
