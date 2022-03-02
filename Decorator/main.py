"""Декоратор - это функция, которая позволяет обернуть другую функцию
для расширения её функциональности без непосредственного изменения её кода."""
def decator(func):
    def wrapper(*args, **kwargs):
        #*args, **kwargs Переменное количество аргументов
        res = func(*args, **kwargs) + 100
        #Действие декоратора, пребовляет 100
        return res

    return wrapper

def plus(func):
    def wrapper(*args, **kwargs):
        #*args, **kwargs Переменное количество аргументов
        res = func(*args, **kwargs) + 200
        #Действие декоратора, пребовляет 200
        return res

    return wrapper

"""Используем один декоратор"""
@decator
def a(x):
    return x + 1 + 1

"""Используем два декоратора"""
@plus
@decator
def b():
    return 5 + 5

@decator
def c():
    return 10 + 10

print(a(2), b(), c())