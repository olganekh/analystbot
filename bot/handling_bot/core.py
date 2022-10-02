from telegram.ext import Updater, CommandHandler
from bot.handling_bot.starrt_command import start
from analyst.settings import TOKEN_TELEGRAM_BOT_API

updater = Updater(TOKEN_TELEGRAM_BOT_API)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
updater.start_polling()
updater.idle()


def run_bot():
    return None