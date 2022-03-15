from unittest import TestCase
import unittest


class MyTestCase(TestCase):
    """
    Развернуть массив

    [1,2,3] -> [3,2,1]
    """

    def test_1(self):
        """
        Решение:
        - Завести массив 1
        - Завести массив 2
        - Взять последний элемент массива из массива 1 три раза положить в новый массив
        - Удалит массив 1
        - Проверить перевернутый массив
        """

        # Завожу массив
        lst = [1, 2, 3]

        lst2 = []

        a = lst.pop()  # 3
        b = lst.pop()  # 2
        c = lst.pop()  # 1

        lst2.append(a)
        lst2.append(b)
        lst2.append(c)

        # Проверяю массив
        self.assertEqual(lst2, [3, 2, 1])

    def test_2(self):
        """
        Решение:
        - Завести массив 1
        - Завести массив 2
        - Взять последний элемент массива из массива 1 три раза положить в новый массив
        - Удалит массив 1
        - Проверить перевернутый массив
        """

        # Завожу массив
        lst = [1, 2, 3]

        lst.append(4)

        lst2 = []

        for i in "xxxx":
            a = lst.pop()
            lst2.append(a)

        # Проверяю массив
        self.assertEqual(lst2, [4, 3, 2, 1])

    def test_3(self):
        """
        Решение:
        - Завести массив 1
        - Завести массив 2
        - Взять последний элемент массива из массива 1 три раза положить в новый массив
        - Удалит массив 1
        - Проверить перевернутый массив
        """

        # Завожу массив
        lst = [1, 2, 3]
        
        lst.append(4)
        lst.append(5)

        lst_len = 5

        lst2 = []

        for i in range(lst_len):
            a = lst.pop()
            lst2.append(a)

        # Проверяю массив
        self.assertEqual(lst2, [5, 4, 3, 2, 1])

    def test_4(self):
        """
        Решение:
        - Завести массив 1
        - Завести массив 2
        - Взять последний элемент массива из массива 1 три раза положить в новый массив
        - Удалит массив 1
        - Проверить перевернутый массив
        """

        # Завожу массив
        lst = [1, 2, 3]
        
        lst.append(4)
        lst.append(5)
        lst.append(6)

        lst_len = len(lst)

        lst2 = []

        for i in range(lst_len):
            a = lst.pop()
            lst2.append(a)

        # Проверяю массив
        self.assertEqual(lst2, [6, 5, 4, 3, 2, 1])


if __name__ == "__main__":
    unittest.main()
