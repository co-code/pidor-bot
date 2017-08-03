# -*- coding: utf-8 -*-
import os
import telebot
from telebot import types

telegram_api_key = os.environ.get("TOKEN")
bot = telebot.AsyncTeleBot(telegram_api_key)


def lambda_handler(event, context):
    try:
        message = types.Message.de_json(eval(event['body'])['message'])
        text = message.text
        if 'ПИДОР' in text.upper():
            task = bot.reply_to(message, 'Слышь, ты сам пидор!')
        if 'НЕТ' in text.upper():
            task = bot.reply_to(message, 'Пидора ответ')
        if 'ДА' in text.upper():
            task = bot.reply_to(message, 'Манда')
        if 'ПОШЕЛ НАХУЙ' in text.upper():
            task = bot.reply_to(message, 'Сам пошел нахуй')
        if 'ГО' in text.upper():
            task = bot.reply_to(message, 'Го по пиву лучше')
        task.wait()
    except Exception:
        print(Exception)
    finally:
        return {"statusCode": 200,
                "body": str(event),
                "headers": {
                    'Content-Type': 'application/json'
                }
                }
