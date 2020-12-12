from telegram.ext import CommandHandler, Updater

from config import PROXY, BOT_TOKEN
import commands


def build_bot():
    """Create bot updater, add handlers."""
    bot = Updater(token=BOT_TOKEN, use_context=True, request_kwargs=PROXY)

    dispatcher = bot.dispatcher

    for name, member in commands.Command.__members__.items():
        handler = CommandHandler(name, getattr(commands, member.value))
        dispatcher.add_handler(handler)

    return bot


if __name__ == '__main__':

    telegram_bot = build_bot()
    telegram_bot.start_polling()
