import html_parser

from telegram.ext import CommandHandler, Updater

from config import REQUEST_KWARGS, BOT_TOKEN, BOT_START_TEXT


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=BOT_START_TEXT)


def get_stat(update, context):
    daily_stat = html_parser.get_daily_stat_message()
    context.bot.send_message(chat_id=update.effective_chat.id, text=daily_stat)

def get_dates(update, context):
    open_countries = html_parser.get_open_countries()
    context.bot.send_message(chat_id=update.effective_chat.id, text=open_countries)

def build_bot():
    bot_updater = Updater(token=BOT_TOKEN, use_context=True, request_kwargs=REQUEST_KWARGS)

    dispatcher = bot_updater.dispatcher

    start_handler = CommandHandler('start', start)
    get_stat_handler = CommandHandler('get_stat', get_stat)
    get_dates_handler = CommandHandler('get_dates', get_dates)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(get_stat_handler)
    dispatcher.add_handler(get_dates_handler)

    return bot_updater


if __name__ == '__main__':

    bot_updater = build_bot()
    bot_updater.start_polling()
