import datetime
from spy import *

def hi_command(update: Update, context: CallbackContext):
  log(update,context)
  update.message.reply_text(f'Привет {update.effective_user.first_name} !')

def help_command(update: Update, context: CallbackContext):
  log(update,context)
  update.message.reply_text(f'/hi\n/time\n/help\n/name (введите имя)\n')

def time_command(update: Update, context: CallbackContext):
  log(update,context)
  today = datetime.datetime.today()
  update.message.reply_text(today.strftime("Сегодня: %d/%m/%Y время: %H.%M:%S"))

def sum_command(update: Update, context: CallbackContext):
  log(update,context)
  msg = update.message.text
  print(msg)
  items = msg.split()
  x = int(eval(items[1]))
  y = int(eval(items[2]))
  update.message.reply_text(f'{x} + {y} = {x + y}')

def name_command(update: Update, context: CallbackContext):
  log(update,context)
  msg = update.message.text
  items = msg.split()
  update.message.reply_text(f"Меня зовут : {items[1]}")


