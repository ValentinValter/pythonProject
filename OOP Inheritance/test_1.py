import unittest
from .main import Sum_multiply

class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = Sum_multiply()
        self.assertEqual(s.add_numb(2), 5)  # add assertion here
        self.assertEqual(s.multiply_numb(2), 10)

if __name__ == '__main__':
    unittest.main()
