import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from location import Location
from zomato import Zomato

TOKEN = "486717629:AAET2FKjId2ehdhUeK-UYjQqkbtW35Musds"
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher





##Fonksiyon

l = Location()
z = Zomato("ba778a4b6afff374876684ada9ddeac1")

def Start(bot, update):
    location_keyboard = telegram.KeyboardButton(text="Konumunu Gönder", request_location=True)
    custom_keyboard = [[location_keyboard]]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    bot.sendMessage(chat_id=update.message.chat_id, text = "Size iyi kalitede hizmet vermemiz için Konumunuzu gönderiniz.",
    reply_markup = reply_markup)

def set_location(bot, update):
    l.set_location(update.message.location)
    bot.sendMessage(chat_id=update.message.chat_id, text=l.get_location()["longitude"])

def deneme(bot, update):
    a = l.get_location()
    print(z.get_City(a["latitude"], a["longitude"]))

##Handler

start_handler = CommandHandler("start", Start)
deneme_handler = CommandHandler("deneme", deneme)


##DISPATCHER

dispatcher.add_handler(start_handler)
dispatcher.add_handler(deneme_handler)
dispatcher.add_handler(MessageHandler(Filters.location, set_location))


updater.start_polling()
