import unittest
from .main import fn

class MyTestCase(unittest.TestCase):
    def test_something(self):
        y = fn()
        self.assertEqual(y, 7)  # add assertion here


if __name__ == '__main__':
    unittest.main()
