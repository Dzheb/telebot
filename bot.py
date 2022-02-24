from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from  bot_commands import *
from config import TOKEN

updater = Updater(TOKEN)

  
updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('time',time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))
updater.dispatcher.add_handler(CommandHandler('name', name_command))

print('server started')

updater.start_polling()
updater.idle()
