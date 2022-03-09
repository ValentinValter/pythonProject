"""
Изучение requests, json, get
requests - это модуль Python, который можно использовать для отправки всех видов HTTP-запросов
json - (JavaScript Object Notation) - это текстовый формат для хранения и обмена данными.
"""

import json

import requests


def fn():
    # Метод get() возвращает значение по указанному ключу.
    # Если указанного ключа не существует, метод вернёт None.
    response = requests.get("https://reqres.in/api/users?page=2")

    # json.loads() метод считывает строку в формате JSON
    # и возвращает объекты Python. Из 'str' в 'dict'.
    data = json.loads(response.text)

    # Получили значение ключа "data" из словаря
    m = data["data"]
    n = m[0]

    return n
