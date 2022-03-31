import sqlite3 as sq
import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        # Подключаемся к базе данных sqlite
        sq_connction = sq.connect('users.db')
        cursor = sq_connction.cursor()

        # Выбор нужных полей из таблицы
        sq_select = """SELECT name from users LIMIT 1"""
        # Выполнить мой запрос
        cursor.execute(sq_select)
        # Получаем данные из sqlite превращаем их в данные python и присваиваем переменную
        records = cursor.fetchall()
        cursor.close()

        self.assertEqual(records, [('Kirpich',)])  # add assertion here


if __name__ == '__main__':
    unittest.main()
