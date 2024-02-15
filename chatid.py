import telebot
from telebot import *
from config import *

bot = telebot.TeleBot(token=TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    id = message.from_user.id
    print(f'{id}')

bot.polling()