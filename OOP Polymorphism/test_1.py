import unittest
from .main import Rectangle, Square

class MyTestCase(unittest.TestCase):
    def test_something(self):
        rect = Rectangle(2, 3)
        sq = Square(5)
        self.assertEqual(rect.get_area(), 6)  # add assertion here
        self.assertEqual(sq.get_area(), 25)

if __name__ == '__main__':
    unittest.main()
