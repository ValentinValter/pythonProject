import unittest

from Rekursiya.main import lst_to_flat


class MyTestCase(unittest.TestCase):
    def test_something(self):
        a = sum(sum([[1, 2, 3, 4], [5, 6, 7], [8, 9, 9]], []))
        self.assertEqual(a, 54)  # add assertion here

    def test_something1(self):
        lst = [1, 2, 3, [4, 5, 6, [7, 8, 9, [10, 11, 12, [13, 14, 15]]]]]
        a = lst_to_flat(lst)
        b = sum(a)
        self.assertEqual(b, 120)  # add assertion here


if __name__ == '__main__':
    unittest.main()
