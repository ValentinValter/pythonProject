"""Изучение requests, json, get
requests - это модуль Python, который можно использовать для отправки всех видов HTTP-запросов
json - (JavaScript Object Notation) - это текстовый формат для хранения и обмена данными."""
import requests
import json

response = requests.get("https://reqres.in/api/users?page=2")
#Метод get() возвращает значение по указанному ключу. Если указанного ключа не существует, метод вернёт None.
print(response.text)
print(type(response.text))
data = json.loads(response.text)
#json.loads() метод считывает строку в формате JSON и возвращает объекты Python. Из 'str' в 'dict'.
print(type(data))
data["page"]
#Получили значение ключа "page" из словаря
print(data["page"])

def fn():
    m = data ["data"]
    n = m[0]
    z = n["id"]
    return z
print(fn())
