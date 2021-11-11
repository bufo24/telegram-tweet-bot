from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from twitter import tweet
from config import token, admin_id
import csv


def tweet_command(update: Update, context: CallbackContext) -> None:
    admins = get_admins()
    sender = str(update.message.from_user.id)
    if (admin_id == int(sender) or admins.__contains__(sender)):
        message = update.message.text.removeprefix("/tweet ")
        try: 
            tweet(message)
            update.message.reply_text(f'Tweeted: {message}')
        except Exception as e:
            update.message.reply_text(f'An error occured: {e}')
    else:
        update.message.reply_text("You are not authorized to use this command.")

def add_command(update: Update, context: CallbackContext) -> None:
    if (update.message.from_user.id == admin_id):
        message = update.message.text.removeprefix("/add ")
        f = open('users.csv','a')
        f.write(f'{message}\n')
        f.close()
        update.message.reply_text("User added to list.")
    else:
        update.message.reply_text("You are not authorized to use this command.")

def admin_command(update: Update, context: CallbackContext) -> list:
    admins = get_admins()
    if (len(admins) == 0):
        update.message.reply_text("No admins found.")
    else:
        sarr = [str(a).lstrip("['").rstrip("']") for a in admins]
        update.message.reply_text(f'Current admins: {", " . join(sarr)}')

def get_admins() -> list:
    with open("users.csv") as file_name:
        file_read = csv.reader(file_name)
        array = list(file_read)
        array = list(map(lambda x: x[0], array))
        return array

updater = Updater(token)

updater.dispatcher.add_handler(CommandHandler('tweet', tweet_command))
updater.dispatcher.add_handler(CommandHandler('add', add_command))
updater.dispatcher.add_handler(CommandHandler('admins', admin_command))

updater.start_polling()
updater.idle()