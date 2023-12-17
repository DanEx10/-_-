from random import choice
from time import sleep

import telebot

bot = telebot.TeleBot('6512595731:AAGBh1ukPVGw6FFy_ex8nKjTXc1oRX45vk4')


@bot.message_handler(commands=['start'])
def start_hi(message):
    sleep(1)
    bot.send_message(message.chat.id, "Привет!")


@bot.message_handler()
def how_are_you(message):
    if message.text.lower() == "как дела?":
        sleep(1)
        bot.send_message(message.chat.id, choice(["Хорошо", "Отлично!", "Нормально"]))
