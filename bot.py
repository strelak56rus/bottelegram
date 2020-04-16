import telebot 
import os

client = telebot.TeleBot('849749831:AAGHdXGorfbGGtY9N8pVWCvYIJie8qlxo-A')

@client.message_handler(content_types=['text'])
def lalala(message):
    client.send_message(message.chat.id, message.text)

# RUN
client.polling()