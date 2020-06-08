from glob import glob
from random import choice
from telebot import apihelper, types
import json

import telebot

ih = open("config.json", "r")
config = json.load(ih)
ih.close()

apihelper.proxy = {'https': 'socks5://learn:python@t2.learn.python.ru:1080'}
TOKEN = config["bot_token"]
bot = telebot.TeleBot(TOKEN)

markup = types.ReplyKeyboardMarkup(row_width=1)
item = types.KeyboardButton('Получить')
markup.row(item)


@bot.message_handler(commands=['start'])
def start(message):
    user = message.chat.id
    bot.send_message(
        user, "Мяу... Ты тоже хочешь фото котика?", reply_markup=markup
        )


@bot.message_handler(regexp='Получить')
def send_picture(message):
    user = message.chat.id
    cat_list = glob('images/cat*.jp*g')
    cat_pic = choice(cat_list)
    bot.send_photo(user, open(cat_pic, 'rb'))
    bot.send_message(
        user, "Еще?...", reply_markup=markup
        )


bot.polling()