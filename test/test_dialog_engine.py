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
            'пидoр': [
                'пидор дед твой',
                'ты сам пидор',
            ],
            'сидoр': [
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


if __name__ == '__main__':
    unittest.main()
