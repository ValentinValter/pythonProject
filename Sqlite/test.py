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
        # Проверяем действительно ли есть такое имя в таблице
        self.assertEqual(records, [('Kirpich',)])  # add assertion here

    def test_something1(self):
        # Подключаемся к базе данных sqlite
        sq_connction = sq.connect('users.db')
        cursor = sq_connction.cursor()

        # Добавляем данные в таблицу
        cur = sq_connction.cursor()
        cur.execute("""INSERT INTO users VALUES("Brus", 16000)""")

        # Выбор нужных полей из таблицы
        sq_select = """SELECT * from users WHERE name = 'Brus'"""
        # Выполнить мой запрос
        cursor.execute(sq_select)
        # Получаем данные из sqlite превращаем их в данные python и присваиваем переменную
        records = cursor.fetchall()
        cursor.close()
        # Проверяем добавление новых данных в таблицу
        self.assertEqual(records, [('Brus', '16000')])  # add assertion here

    def test_something2(self):
        # Подключаемся к базе данных sqlite
        sq_connction = sq.connect('users.db')
        cursor = sq_connction.cursor()

        # изменяем данные в таблице
        cur = sq_connction.cursor()
        cur.execute("""UPDATE users SET price = 199 WHERE name = 'Kirpich'""")

        # Выбор нужных полей из таблицы
        sq_select = """SELECT price from users WHERE rowid = 1"""
        # Выполнить мой запрос
        cursor.execute(sq_select)
        # Получаем данные из sqlite превращаем их в данные python и присваиваем переменную
        records = cursor.fetchall()
        cursor.close()
        # Проверяем изменения в таблице
        self.assertEqual(records, [('199',)])  # add assertion here

    def test_something3(self):
        # Подключаемся к базе данных sqlite
        sq_connction = sq.connect('users.db')
        cursor = sq_connction.cursor()

        # Удаляем данные в таблице
        cur = sq_connction.cursor()
        cur.execute("""DELETE FROM users WHERE rowid IN(1)""")

        # Выбор нужных полей из таблицы
        sq_select = """SELECT * from users WHERE rowid = 1"""
        # Выполнить мой запрос
        cursor.execute(sq_select)
        # Получаем данные из sqlite превращаем их в данные python и присваиваем переменную
        records = cursor.fetchall()
        cursor.close()
        # Проверяем удаление данных в таблице
        self.assertEqual(records, [])  # add assertion here


if __name__ == '__main__':
    unittest.main()
