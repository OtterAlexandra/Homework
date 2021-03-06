import logging
from telegram.ext import Updater, MessageHandler, Filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

TOKEN = '5269000390:AAEf01m-t20HvceQOWH_Zn5a1ew7URjs1AU'


def echo(update, context):
    update.message.reply_text(update.message.text)


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    text_handler = MessageHandler(Filters.text, echo)
    dp.add_handler(text_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
