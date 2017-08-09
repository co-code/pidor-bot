# -*- coding: utf-8 -*-
import unittest

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
                'ну пока',
                'ну и пиздуй'
            ],
            'пизда': [
                'не ругайся!'
            ],
            'да': [
                'манда',
                'хуй на'
            ],
            'нет': [
                'пидора ответ'
            ],
            'пидор': [
                'пидор дед твой',
                'ты сам пидор',
            ],
            'сидор': [
                'это я люблю',
            ],
            'го': [
                'го по пиву лучше '
            ],
            'го гулять': [
                'го по пиву лучше '
            ],
            '))))': [
                '))))))))))))',
                'гы))))'
            ]
        }
        
        for k, v in ls.items():
            answer = self.de.choose_answer(k)
            print(k, v, answer)
            self.assertTrue(answer in v)

    def test_some_case_insensitive(self):
        ls = {
            'Привет': [
                'ну привет',
                'тебя не звали, иди отсюда'
            ],
            'ПрИвЕт': [
                'ну привет',
                'тебя не звали, иди отсюда'
            ],
            'Пока': [
                'ну пока',
                'ну и пиздуй'
            ],
            'пиЗда': [
                'не ругайся!'
            ],
            'Да': [
                'манда',
                'хуй на'
            ],
            'Нет': [
                'пидора ответ'
            ],
            'пИдОр': [
                'пидор дед твой',
                'ты сам пидор',
            ],
            'сидОр': [
                'это я люблю',
            ],
            'Го': [
                'го по пиву лучше '
            ],
            'гО гулять': [
                'го по пиву лучше '
            ]
        }

        for k, v in ls.items():
            answer = self.de.choose_answer(k)
            print(k, v, answer)
            self.assertTrue(answer in v)

if __name__ == '__main__':
    unittest.main()
