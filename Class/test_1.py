import unittest
from .main import Calc

class MyTestCase(unittest.TestCase):
    def test_something(self):
        y = Calc()
        self.assertEqual(y.add_numb(2), 4)  # add assertion here


if __name__ == '__main__':
    unittest.main()
