import html_parser
import info

BOT_START_TEXT = "Hi! I'm bot, who knows a few statistic about COVID-19 in Russia." \
                 "\nUse info: " \
                 "\n/statistic - get current statistic. " \
                 "\n/boarders - get dates when boarders will be opened."


def start(update, context):
    """Greet user on start command."""
    context.bot.send_message(chat_id=update.effective_chat.id, text=BOT_START_TEXT)


def get_statistic(update, context):
    """Show COVID statistic."""
    daily_stat = info.get_statistic()
    context.bot.send_message(chat_id=update.effective_chat.id, text=daily_stat)


def get_open_boarder_dates(update, context):
    """Show dates of opening boarders."""
    open_countries = html_parser.get_open_countries()
    context.bot.send_message(chat_id=update.effective_chat.id, text=open_countries)
