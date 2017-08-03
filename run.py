# -*- coding: utf-8 -*-
import os
import telebot
import random
import json

telegram_api_key = os.environ.get("TOKEN")
bot = telebot.TeleBot(telegram_api_key)


def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        message = telebot.types.Message.de_json(body['message'])
        text = message.text
        words = text.upper().split(' ')
        if 'ПИДОР' in words:
            bot.reply_to(message, random.choice(['слышь, ты сам пидор', 'сам пидор']))
        if 'CИДОР' in words:
            bot.reply_to(message, random.choice(['это я люблю']))
        if 'НЕТ' in words:
            bot.reply_to(message, random.choice(['пидора ответ']))
        if 'ДА' in words:
            bot.reply_to(message, random.choice(['манда', 'хуй на']))
        if 'ПОШЕЛ НАХУЙ' in words:
            bot.reply_to(message, random.choice(['сам пошел нахуй']))
        if 'ГО' in words:
            bot.reply_to(message, random.choice(['го по пиву лучше']))
        if ')' in text:
            bot.reply_to(message, random.choice(['гы)))', '))))))))))))))))))))))']))
    except Exception as e:
        print(str(e))
        print(str(event))
    finally:
        return {"statusCode": 200,
                "body": str(event),
                "headers": {
                    'Content-Type': 'application/json'
                }
                }
