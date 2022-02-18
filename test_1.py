import unittest
from main import add_numb

class MyTestCase(unittest.TestCase):
    def test_something(self):
        y = add_numb(2)
        self.assertEqual(y, 4)  # add assertion here


if __name__ == '__main__':
    unittest.main()
