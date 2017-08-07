# -*- coding: utf-8 -*-
import unittest

from telebot.types import Message
from dialog.engine import DialogEngine


class TestDialogEngine(unittest.TestCase):
    def setUp(self):
        self.de = DialogEngine()

    def test_some_answers(self):
        ls = {
            'привет': [
                'ну привет',
                'тебя не звали, иди отсюда'
            ],
            'пока': [
                'ну и пиздуй',
            ],
            'пизда': [
                'не ругайся!',
                'где?'
            ],
            'да': [
                'манда',
                'хуй на'
            ],
            'нет': [
                'пидора ответ'
            ],
            'пидoр': [
                'пидор твой дед',
                'ты сам пидор',
                'пойдем пить сидор'
            ],
            'сидoр': [
                'это я люблю',
                'кто не пьет, тот пидор'
            ],
            'го': [
                'го к еноту',
                'го пить сидор',
                'го бухать',
                'го калик курить'
            ],
            '))))': [
                'гы))))'
            ]
        }

        for k, v in ls.items():
            answer = self.de.choose_answer(k)
            print(k, v, answer)
            self.assertTrue(answer in v)


if __name__ == '__main__':
    unittest.main()
