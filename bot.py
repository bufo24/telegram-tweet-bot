from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from twitter import tweet
from auth import token


def tweetCommand(update: Update, context: CallbackContext) -> None:
    message = update.message.text.removeprefix("/tweet ")
    tweet(message)
    update.message.reply_text(f'Tweeted: {message}')


updater = Updater(token)

updater.dispatcher.add_handler(CommandHandler('tweet', tweetCommand))

updater.start_polling()
updater.idle()