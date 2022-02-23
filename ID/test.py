import unittest
import copy

class MyTestCase(unittest.TestCase):
    def test_something(self):
        """Одинаковые id у переменных"""

        a = [1, 2, 3]
        b = a
        print(id(a))
        print(id(b))
        self.assertEqual(id(a), id(b))  # add assertion here

    def test_something1(self):
        """Делаем разное id у переменных"""
        x = [1, 2, 3, 4]
        y = x
        y = copy.copy(x)
        print(id(x))
        print(id(y))
        self.assertNotEqual(id(x), id(y))  # add assertion here
if __name__ == '__main__':
    unittest.main()
