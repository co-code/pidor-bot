# -*- coding: utf-8 -*-
import json
import os
import telebot

from util.log_helper import log
from util.example_event import example
from dialog.engine import DialogEngine


def init():
    global bot
    global dialog_engine

    dialog_engine = DialogEngine()

    telegram_api_key = os.environ.get('TOKEN')
    bot = telebot.TeleBot(telegram_api_key)


def lambda_handler(event, context, offline_mode=False):
    try:
        log('Event: ' + str(event))
        body = json.loads(event['body'])
        message = telebot.types.Message.de_json(body['message'])
        answer = dialog_engine.choose_answer(message)
        if not offline_mode:
            bot.reply_to(message, answer)
        else:
            log('Answer: ' + str(answer))

    except Exception as e:
        log('Error: ' + str(e))

    return {
        'statusCode': 200,
        'body': str(event),
        'headers': {
            'Content-Type': 'application/json'
        }
    }


init()

if __name__ == '__main__':
    lambda_handler(event=example, context=None, offline_mode=True)
