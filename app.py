import telebot

bottoken = "1836057993:AAF4cP9qNx3gFh-epkgjBRYkALyzVs6W0gw"

bot = telebot.TeleBot(bottoken)

@bot.message_handler(commands=["start","hello"])
def send_wlcomemesssage(message):
    bot.reply_to(message,"Hello")


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()