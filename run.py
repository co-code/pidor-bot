# -*- coding: utf-8 -*-
import os
import telebot
import random
import json
import re
import logging


def init():
    global bot
    global logger
    global data

    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '[%(levelname)5s] (%(threadName)s) - %(asctime)-15s : %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

    logger = logging.getLogger('pidor-bot')

    with open('answers.json', encoding='utf-8') as f:
        data = json.loads(f.read())

    telegram_api_key = os.environ.get('TOKEN')
    bot = telebot.TeleBot(telegram_api_key)


def lambda_handler(event, context):
    try:
        logger.debug(event)

        body = json.loads(event['body'])
        message = telebot.types.Message.de_json(body['message'])
        text = message.text

        logger.info(text)

        for question, answers in data:
            if re.match(question, text):
                bot.reply_to(message, random.choice(answers))

        return {
            'statusCode': 200,
            'body': str(event),
            'headers': {
                'Content-Type': 'application/json'
            }
        }

    except Exception as e:
        logger.error(e)

        return {
            'statusCode': 500,
            'body': str(e),
            'headers': {
                'Content-Type': 'application/json'
            }
        }


init()
