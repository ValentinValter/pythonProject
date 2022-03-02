"""Изучение тип данных (Data Type)"""
import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        """Тип данных: числа Numbers"""

        a = 1
        b = isinstance(a, int)
        self.assertTrue(b)  # add assertion here

    def test_something1(self):
        """Тип данных: строки (Strings)"""

        a = 'bb'
        b = isinstance(a, str)
        self.assertTrue(b)  # add assertion here

    def test_something2(self):
        """Тип данных: список (List)"""

        a = [1, 'asdf', 20]
        b = isinstance(a, list)
        self.assertTrue(b)  # add assertion here

    def test_something3(self):
        """Тип данных: Словарь (dict)"""

        a = {
            'City1': 'Красноярск',
            'City2': 'Улан-Удэ',
            'City3': 'Новосибирск'
        }
        b = isinstance(a, dict)
        self.assertTrue(b)  # add assertion here

    def test_something4(self):
        """Тип данных: Кортеж (Tuple) """

        list_keys = [10, 20, 'asdf']
        tuple1 = tuple(list_keys)
        b = isinstance(tuple1, tuple)
        self.assertTrue(b)  # add assertion here

    def test_something5(self):
        """Тип данных: Множество (Set) - убирает одинаковые значения"""

        list_keys = [10, 20, 'asdf', 30, 40, 10, 20]
        set1 = set(list_keys)
        b = isinstance(set1, set)
        self.assertTrue(b)  # add assertion here
if __name__ == '__main__':
    unittest.main()
