import info

BOT_START_TEXT = "Hi! I'm bot, who knows a few statistic about COVID-19 in Russia." \
                 "\nUse info: " \
                 "\n/statistic - get current statistic. " \
                 "\n/news - get last news about COVID-19."


def start(update, context):
    """Greet user on start command."""
    context.bot.send_message(chat_id=update.effective_chat.id, text=BOT_START_TEXT)


def get_statistic(update, context):
    """Show COVID statistic."""
    daily_stat = info.get_statistic()
    context.bot.send_message(chat_id=update.effective_chat.id, text=daily_stat)


def get_last_news(update, context):
    """Show dates of opening boarders."""
    last_news = info.get_last_news()
    for news in last_news:
        context.bot.send_message(chat_id=update.effective_chat.id, text=news)
