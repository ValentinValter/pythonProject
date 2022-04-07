import sqlite3 as sq
import unittest


def select(x, y):
    # Подключаемся к базе данных sqlite
    sq_connction = sq.connect('users.db')
    cursor = sq_connction.cursor()

    # Выбор полей из таблицы
    sq_select = "SELECT " + x + " from users " + y
    # Выполнить мой запрос
    cursor.execute(sq_select)
    # Получаем данные из sqlite превращаем их в данные python и присваиваем переменную
    records = cursor.fetchall()
    return records


class MyTestCase(unittest.TestCase):
    """Методы setUp() и tearDown() позволяют определять инструкции,
    выполняемые перед и после каждого теста, соответственно."""

    def setUp(self) -> None:
        # Подключаемся к базе данных sqlite
        sq_connction = sq.connect('users.db')
        cursor = sq_connction.cursor()

        # создаем таблицу
        cursor.execute("""CREATE TABLE users (
            name TEXT,
            price INTEGER)""")

        # Добавляем данные в таблицу
        cursor.execute("""INSERT INTO users VALUES("Kirpich", 500)""")

        # Сохраняем в базе данных
        sq_connction.commit()

    def tearDown(self) -> None:
        # Подключаемся к базе данных sqlite
        sq_connction = sq.connect('users.db')
        cursor = sq_connction.cursor()

        # Удаляем все данные в таблице
        cursor.execute("""DROP TABLE users""")
        # Сохраняем в базе данных
        sq_connction.commit()

    def test_something(self):
        # Выбор нужных полей из таблицы
        y = select("name", "LIMIT 1")
        # Проверяем действительно ли есть такое имя в таблице
        self.assertEqual(y, [('Kirpich',)])  # add assertion here

    def test_something1(self):
        # Подключаемся к базе данных sqlite
        sq_connction = sq.connect('users.db')

        # Добавляем данные в таблицу
        cur = sq_connction.cursor()
        cur.execute("""INSERT INTO users VALUES("Brus", 16000)""")

        # Сохраняем в базе данных
        sq_connction.commit()

        # Выбор нужных полей из таблицы
        y = select("*", "WHERE name = 'Brus'")
        # Проверяем добавление новых данных в таблицу
        self.assertEqual(y, [('Brus', 16000)])  # add assertion here

    def test_something2(self):
        # Подключаемся к базе данных sqlite
        sq_connction = sq.connect('users.db')

        # изменяем данные в таблице
        cur = sq_connction.cursor()
        cur.execute("""UPDATE users SET price = 199 WHERE name = 'Kirpich'""")
        # Сохраняем в базе данных
        sq_connction.commit()

        # # Выбор нужных полей из таблицы
        y = select("price", "WHERE name = 'Kirpich'")

        # Проверяем изменения в таблице
        self.assertEqual(y, [(199,)])  # add assertion here

    def test_something3(self):
        # Подключаемся к базе данных sqlite
        sq_connction = sq.connect('users.db')
        cursor = sq_connction.cursor()

        # Удаляем данные в таблице
        cur = sq_connction.cursor()
        cur.execute("""DELETE FROM users WHERE rowid IN(2)""")

        # Сохраняем в базе данных
        sq_connction.commit()

        # Выбор нужных полей из таблицы
        y = select("*", "WHERE rowid = 2")
        # Проверяем удаление данных в таблице
        self.assertEqual(y, [])  # add assertion here


if __name__ == '__main__':
    unittest.main()
