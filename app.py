import telebot
import os
from get import get_truecaller_info
from check import is_user_in_channel

bottoken = os.environ['bottoken']

bot = telebot.TeleBot(bottoken)

@bot.message_handler(commands=["start","hello","help"])
def send_wlcomemesssage(message):
    bot.reply_to(message,"Hey I Will Help You to find Phone Numbers Details just send phone number in international format eg:-  +919999999999")


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    # i need to remove spacese from message and convert it to string
    phone_numbert = message.text.replace(" ", "")
    # get sender id
    sender_id = message.chat.id
    # check if the user is in the channel
    if not is_user_in_channel(sender_id):
        bot.reply_to(message, "Please join the channel to use this bot @pkdart")
        return
    # check if the message is a number with + sign
    if phone_numbert.startswith("+") and phone_numbert[1:].isdigit():
        dtails = get_truecaller_info(phone_numbert)
        bot.reply_to(message, dtails)
    else:
        bot.reply_to(message, "Please send a valid phone number")


bot.infinity_polling()
