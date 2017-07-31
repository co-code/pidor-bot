import telebot

bot = telebot.TeleBot("242501698:AAFrulS4H9AaycbFUAJPhXz5No6ibmhxIys")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    user = message.from_user
    text = message.text
    if 'ПИДОР' in text.upper():
        bot.reply_to(message, 'Слышь, ты сам пидор!')


bot.polling()
