from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from twitter import tweet


def tweetCommand(update: Update, context: CallbackContext) -> None:
    message = update.message.text.removeprefix("/tweet ")
    tweet(message)
    update.message.reply_text(f'Tweeted: {message}')


updater = Updater('2124765915:AAHh81Emvzca2OlneTiKpwzJELlDxO_MAjk')

updater.dispatcher.add_handler(CommandHandler('tweet', tweetCommand))

updater.start_polling()
updater.idle()