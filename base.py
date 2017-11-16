import telegram
from telegram.ext import Updater, CommandHandler

TOKEN = "486717629:AAET2FKjId2ehdhUeK-UYjQqkbtW35Musds"
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher


##Fonksiyon

def Start(bot, update):
    location_keyboard = telegram.KeyboardButton(text="send_location", request_location=True)
    contact_keyboard = telegram.KeyboardButton(text="send_contact", request_contact=True)
    custom_keyboard = [[location_keyboard, contact_keyboard]]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    bot.sendMessage(chat_id=update.message.chat_id, text = "Would you mind sharing your location and contact with me?",
    reply_markup = reply_markup)



##Handler

start_handler = CommandHandler("start", Start)



##DISPATCHER

dispatcher.add_handler(start_handler)

updater.start_polling()
