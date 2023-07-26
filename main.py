# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import logging
import telebot
from responses import *


API_TOKEN = "6386415843:AAE2m111aI-PYG4tF9MyDLVpLOVrWafQAuc"

bot = telebot.TeleBot(API_TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am ThunderDoBot. I am here to moderate you unruly humans.\
""")\

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, """\
No help will be provided...\
""")

@bot.message_handler(commands=['custom'])
def send_welcome(message):
    bot.reply_to(message, """\
Still working on this one...\
""")



# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):

    res = find_bad_words(message.text.lower())
    if res:

        cap_america_language_gif = "https://media.tenor.com/cYN46acNMTQAAAAC/captain-america.gif"

        # bot.reply_to(message, 'watch your language...')
        bot.send_animation(message.chat.id, cap_america_language_gif, reply_to_message_id=message.id)
        # bot.reply_to(message, telebot.formatting.mbold(message.text))


bot.infinity_polling()