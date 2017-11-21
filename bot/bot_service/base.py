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
    l.set_location(update.message.location)##setting location 
    bot.sendMessage(chat_id=update.message.chat_id, text=l.get_location()["longitude"])

def deneme(bot, update):
    a = l.get_location()
    print(z.get_City(a["latitude"], a["longitude"]))

def money_to_eat(bot,update):
    location_data = l.get_location()
    if location_data == None:
        bot.sendMessage(chat_id=update.message.chat_id, text="Lutfen konumuzu gonderiniz . :))")

    else:
        money_count = update.message.text.split(' ')
        data = z.get_nearby_location(location_data,money_count)
        bot.sendMessage(chat_id=update.message.chat_id, text=str(data))

def test2(bot,update):
    print("LLaaa")
    x = update.message.photo[2].file_id
    print(x)

##Handler

start_handler = CommandHandler("start", Start)
deneme_handler = CommandHandler("deneme", deneme)
money_to_eat = CommandHandler("w2e",money_to_eat)

##DISPATCHER

dispatcher.add_handler(start_handler)
dispatcher.add_handler(deneme_handler)
dispatcher.add_handler(money_to_eat)
dispatcher.add_handler(MessageHandler(Filters.location, set_location))
dispatcher.add_handler(MessageHandler(Filters.photo, test2))


updater.start_polling()
