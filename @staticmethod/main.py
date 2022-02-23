"""Статикметод @staticmethod - независимая функция которая работает с параметрами записанными непосредственно
в ней. Эта функция не обращаеться к атрибутам класса и локальным атрибутам экзепляра класса"""

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b

class Square:
    def __init__(self, a):
        self.a = a

    def get_area(self):
        return self.a**2

    @staticmethod
    def plus(x, y):
        return x + y

rect = Rectangle(2, 3)
sq = Square(5)
print(rect.get_area())
print(sq.get_area())
print(sq.plus(3, 7))
