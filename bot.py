import telebot 
import os

token = os.environ.get('849749831:AAGHdXGorfbGGtY9N8pVWCvYIJie8qlxo-A')
bot = telebot.Telebot(str(token))

@bot.message_handler(content_types=['text'])
def lalala(message):
    bot.send_message(message.chat.id, message.text)

# RUN
bot.polling()
