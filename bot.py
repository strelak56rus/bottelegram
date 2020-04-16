import telebot 
import os

token = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(str(token))

@bot.message_handler(content_types=['text'])
def lalala(message):
    bot.send_message(message.chat.id, message.text)

# RUN
bot.polling()
