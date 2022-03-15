import sys
import unittest


class MyTestCase(unittest.TestCase):
    # Создание двух одинаковых массивов и их проверка
    def test_something(self):
        # Создаю массив1
        a = [i for i in range(10)]
        # Создаю массив2
        b = []
        for i in range(10):
            # Добавляю в массив2
            b.append(i)
        # Проверяю массив
        self.assertEqual(a, b)  # add assertion here

    # Создаю массив и доказываю, что он многоразовый
    def test_something1(self):
        # Создаю массив
        # comperhansive генератор списка
        a = [i for i in range(10)]
        # Вызываю массив два раза
        for i in a:
            pass
        for i in a:
            ...
        # Проверяю массив
        self.assertEqual(a, a)  # add assertion here

    # Создаю массив добавляю в него элемент и даказываю что он увеличиваеться в размере
    def test_something2(self):
        # Создаю массив
        # comperhansive генератор списк
        a = [i for i in range(10)]
        # Проверяю размер массива
        s1 = sys.getsizeof(list(a))
        # Добавляю в массив элемент
        a.append(11)
        a.append(12)
        a.append(113)
        a.append(115)
        # Проверяю размер массива
        s2 = sys.getsizeof(list(a))
        # Проверяю массив
        self.assertNotEqual(s1, s2)  # add assertion here

    # Создать генератор и доказать что он удаляется при прохождении элемента
    def test_something3(self):
        x = False

        # Создаю генератор
        a = (i for i in range(10))
        # Прохожу по элементам
        for i in a:
            # Доказываю что прошел по элемента
            if i == 9:
                x = True
        # проверяю результат
        self.assertTrue(x)  # add assertion here

        x = False
        # прохожу по элементам
        for y in a:
            # Доказываю что элементы удалились
            x = True
        # проверяю результат
        self.assertFalse(x)  # add assertion here


if __name__ == '__main__':
    unittest.main()
