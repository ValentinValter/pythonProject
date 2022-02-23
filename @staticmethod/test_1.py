import unittest
from .main import Rectangle, Square

class MyTestCase(unittest.TestCase):
    def test_something(self):
        """С иницилизацией класса"""
        rect = Rectangle(2, 3)
        sq = Square(5)
        self.assertEqual(rect.get_area(), 6)  # add assertion here
        self.assertEqual(sq.get_area(), 25)
        self.assertEqual(sq.plus(3, 7), 10)

    def test_something1(self):
        """Без иницилизации класса вызываем функцию Plus"""
        self.assertEqual(Square.plus(3, 7), 10)

if __name__ == '__main__':
    unittest.main()
