import telebot 
import os

from telebot import types

token = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(str(token))


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("❗️ Информация")
    item2 = types.KeyboardButton("❗️ Наш ВКонтакте")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, 'Добро пожаловать, выбери нужную опцию.', reply_markup=markup)

def mainmenu(message):
    if message.chat.type == 'private':
        if message.text == '❗️ Информация':
            bot.send_message(message.chat.id, "Привет")
        elif message.text == '❗️ Наш ВКонтакте':
            bot.send_message(message.chat.id, "https://vk.com/ccoin.shop")


# RUN
bot.polling()
