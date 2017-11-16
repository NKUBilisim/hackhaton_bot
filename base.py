import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from location import Location
TOKEN = "486717629:AAET2FKjId2ehdhUeK-UYjQqkbtW35Musds"
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher





##Fonksiyon

l = Location()

def Start(bot, update):
    location_keyboard = telegram.KeyboardButton(text="send_location", request_location=True)
    contact_keyboard = telegram.KeyboardButton(text="/send_contact", request_contact=True)
    custom_keyboard = [[location_keyboard, contact_keyboard]]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    bot.sendMessage(chat_id=update.message.chat_id, text = "Would you mind sharing your location and contact with me?",
    reply_markup = reply_markup)
    update.message.reply_text('Hello World!')

def set_location(bot, update):
    l.set_location(update.message.location)

def deneme(bot, update):
    print(l.get_location())

##Handler

start_handler = CommandHandler("start", Start)
deneme_handler = CommandHandler("deneme", deneme)


##DISPATCHER

dispatcher.add_handler(start_handler)

dispatcher.add_handler(deneme_handler)


dispatcher.add_handler(MessageHandler(Filters.location, set_location))
updater.start_polling()
