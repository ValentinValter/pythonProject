import unittest
from .main import fn

class MyTestCase(unittest.TestCase):
    def test_something(self):
        y = fn()
        self.assertEqual(y["id"], 7)  # add assertion here

    def test_something1(self):
        y = fn()
        self.assertEqual(y["email"], 'michael.lawson@reqres.in')


if __name__ == '__main__':
    unittest.main()
