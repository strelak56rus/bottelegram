import telebot 
import os

from telebot import types

token = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(str(token))

@bot.message_handler(content_types=['text'])

def lalala(message):
    bot.send_message(message.chat.id, message.text)

@bot.message_handler(content_types=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Информация")
    item2 = types.KeyboardButton("Наш ВКонтакте")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Добро пожаловать, выбери нужную опцию.", reply_markup=markup)



# RUN
bot.polling()
