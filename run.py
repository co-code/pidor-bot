import telebot
import re
import random

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
    if 'НЕТ' in text.upper():
        bot.reply_to(message, 'Пидора ответ')
    if 'ДА' in text.upper():
        bot.reply_to(message, 'Манда')
    if re.search(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text):
        bot.reply_to(message, 'Боян')
    if 'ПОШЕЛ НАХУЙ' in text.upper():
        bot.reply_to(message, 'Сам пошел нахуй')
    if 'ГО' in text.upper():
        bot.reply_to(message, 'Го по пиву лучше')


@bot.message_handler(content_types=['document', 'audio', 'photo'])
def handle_docs(message):
    bot.reply_to(message, random.choice(['ну и хуйня!', "дерьмище", "срань господня", "что за залупа?"
                                         , "лучше бы ты эту хуйню не присылал"]))


bot.polling()
