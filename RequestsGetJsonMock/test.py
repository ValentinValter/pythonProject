"""Изучение Mock"""
import unittest
from .main import fn
from unittest.mock import patch


class MyTestCase(unittest.TestCase):
    # Patch заменяет результат функции fn на mock_fn.return_value = 7
    # Обязательно указывать полный путь.
    @patch("RequestsGetJsonMock.main.fn")
    def test_something(self, mock_fn):
        mock_fn.return_value = 7
        y = fn()
        self.assertEqual(y["id"], 7)  # add assertion here

    # Тест без Mock
    def test_something1(self):
        y = fn()
        self.assertEqual(y["email"], 'michael.lawson@reqres.in')


if __name__ == '__main__':
    unittest.main()
