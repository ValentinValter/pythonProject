import unittest
from .main import decator, plus


class MyTestCase(unittest.TestCase):
    def test_something(self):
        @decator
        def a(x):
            return x + 1 + 1
        self.assertEqual(a(2), 104)  # add assertion here

    def test_something1(self):
        @plus
        @decator
        def b():
            return 5 + 5
        self.assertEqual(b(), 310)

    def test_something2(self):
        @decator
        def c():
            return 10 + 10

        self.assertEqual(c(), 120)

if __name__ == '__main__':
    unittest.main()
