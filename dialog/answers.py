# -*- coding: utf-8 -*-
data = {
    r'(?i)^привет\W*$': [
        'ну привет',
        'тебя не звали, иди отсюда'
    ],
    r'(?i)^пока\W*$': [
        'ну пока',
        'ну и пиздуй'
    ],
    r'(?i)^пизда\W*$': [
        'не ругайся!'
    ],
    r'(?i)^да\W*$': [
        'манда',
        'хуй на'
    ],
    r'(?i)^нет\W*$': [
        'пидора ответ'
    ],
    r'(?i)^пид[о?]р\W*$': [
        'пидор дед твой',
        'ты сам пидор'
    ],
    r'(?i)^сид[о?]р\W*$': [
        'это я люблю'
    ],
    r'(?i)^го': [
        'го по пиву лучше '
    ],
    r'(?:[^(]*\))|(?:.*\)\))\W*$': [
        '))))))))))))',
        'гы))))'
    ],
    r'(?:\()|(?:.*\(\()[^)]*$': [
        '(((((((((((('
    ]
}
