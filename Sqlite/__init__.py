"""изучение SQlite"""
import sqlite3 as sq
#Подключаемся к базе данных sqlite
sq_connction = sq.connect('users.db')
cursor = sq_connction.cursor()

#Выбор всех полей из таблицы
sq_select = """SELECT * from users"""
#Выполнить мой запрос
cursor.execute(sq_select)
#Получаем данные из sqlite превращаем их в данные python и присваиваем переменную
records = cursor.fetchall()
print(records)
cursor.close()
