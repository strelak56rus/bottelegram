import telebot 
import os
import random

from telebot import types

token = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(str(token))


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("✉️ Информация")
    item2 = types.KeyboardButton("📡 Наш ВКонтакте")
    item3 = types.KeyboardButton("💵 Профиль")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, 'Добро пожаловать, выбери нужную кнопку.', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def general(message):
    if message.chat.type == 'private':
        if message.text == '✉️ Информация':
            bot.send_message(message.chat.id, "Информация: Это игровой бот с валютой APPLECOIN, вы можете кликать эту валюту, и её можно обменять на CoronaCoin, и на другие валюты. Успей заработать много AC, и поделиться с другими людьми!")
        elif message.text == '📡 Наш ВКонтакте':
            bot.send_message(message.chat.id, "Мы в ВКонтакте: https://vk.com/ccoin.shop")
        

        elif message.text == '💵 Профиль':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("📈 Курс AppleCoin")
            item2 = types.KeyboardButton("🍏 Клик")
            item3 = types.KeyboardButton("✅ Баланс")
            markup.add(item1, item2, item3)
            bot.send_message(message.chat.id, 'Привет, ты находишься в профиле, выбери то, что тебе нужно', reply_markup=markup)
        elif message.text == '📈 Курс AppleCoin':
            bot.send_message(message.chat.id, '1000 AC = 1 000 000 CoronaCoin | 1 руб = 5 000 AC')
        elif message.text == '🍏 Клик':
            bot.send_message(message.chat.id, 'В разработке')
        elif message.text == '✅ Баланс':
            bot.send_message(message.chat.id, 'Баланс: 0 AC')


        else:
            bot.send_message(message.chat.id, "Ошибка, такая команда не существует.")


# RUN
bot.polling()
