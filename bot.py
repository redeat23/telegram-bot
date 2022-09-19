#from telegram import Bot

#bot = Bot('5563801027:AAENFimrw-wQvGAyYp-8xY4v72pRStu6Fx4')
#print(bot.get_me())
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.updater import Updater
from telegram.ext.dispatcher import Dispatcher
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.bot import Bot
updater = Updater('5563801027:AAENFimrw-wQvGAyYp-8xY4v72pRStu6Fx4',
                  use_context=True)
dispatcher: Dispatcher = updater.dispatcher

def start(update: Update, context: CallbackContext):
    """
    the callback for handling start command
    """
    # getting the bot from context
    # documentation: https://python-telegram-bot.readthedocs.io/en/latest/telegram.bot.html#telegram-bot
    bot: Bot = context.bot
    # sending message to the chat from where it has received the message
    # documentation: https://python-telegram-bot.readthedocs.io/en/latest/telegram.bot.html#telegram.Bot.send_message
    bot.send_message(chat_id=update.effective_chat.id,
                     text="You have just entered start command")

# register a handler (here command handler)
# documentation: https://python-telegram-bot.readthedocs.io/en/latest/telegram.ext.dispatcher.html#telegram.ext.Dispatcher.add_handler
dispatcher.add_handler(
    # it can accept all the telegram.ext.Handler, CommandHandler inherits Handler class
    # documentation: https://python-telegram-bot.readthedocs.io/en/latest/telegram.ext.commandhandler.html#telegram-ext-commandhandler
    CommandHandler("start", start))
# starting polling updates from Telegram
# documentation: https://python-telegram-bot.readthedocs.io/en/latest/telegram.ext.updater.html#telegram.ext.Updater.start_polling
updater.start_polling()