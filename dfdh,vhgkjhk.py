
from flask import Flask, request
import logging

import json

    if req['request']['original_utterance'].lower() in [
        'ладно',
        'да',
        'хочу',
        'хорошо'
    ]:
        res['response']['text'] = 'Ты можешь стоть 10 Хокаге!'
        res['response']['end_session'] = True
        return

    res['response']['text'] = \
        f"Все говорят '{req['request']['original_utterance']}',но нам нужен такой такой Хокаге как ты!"
    res['response']['buttons'] = get_suggests(user_id)

def get_suggests(user_id):
    session = sessionStorage[user_id]

    # Выбираем две первые подсказки из массива.
    suggests = [
        {'title': suggest, 'hide': True}
        for suggest in session['suggests'][:2]
    ]

    # Убираем первую подсказку, чтобы подсказки менялись каждый раз.
    session['suggests'] = session['suggests'][1:]
    sessionStorage[user_id] = session

    # Если осталась только одна подсказка, предлагаем подсказку
    # со ссылкой на Яндекс.Маркет.
    if len(suggests) < 2:
        suggests.append({
            "title": "Ладно",
            "url": "https://market.yandex.ru/search?text= Naruto",
            "hide": True
        })

    return suggests


if __name__ == '__main__':
    app.run()