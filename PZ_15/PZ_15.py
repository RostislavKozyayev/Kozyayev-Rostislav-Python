# Приложение ТОРГОВАЯ ФИРМА для автоматизированного контроля продаж
# товаров торговой фирмы. БД должна содержать таблицу Продажа товаров со следующей
# структурой записи: Дата продажи, Товар, Сумма, Скидка, Филиал, Менеджер.

import sqlite3 as sq

with sq.connect("trading_company.db") as con:
    # Создание таблицы
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS items_sale")
    cur.execute("""CREATE TABLE IF NOT EXISTS items_sale (
    s_id INTEGER PRIMARY KEY,
    sale_date DATE NOT NULL,
    product TEXT NOT NULL,
    price INTEGER NOT NULL,
    discount INTEGER,
    branch TEXT NOT NULL,
    manager VARCHAR(60) NOT NULL)""")

    # Добавление данных в таблицу
    cur.execute("""INSERT INTO items_sale VALUES(1 ,2025-08-25, 'Агуша с яблоком', 
    12599, 15, 'Пятёрочка', 'Евгений Васильевич Костромской')""")
    cur.execute("""INSERT INTO items_sale VALUES(2, 2008-10-12, 'Наручники', 
    1500, 5, 'Магнит', 'Наталья Эдуардовна Будапешт')""")
    cur.execute("""INSERT INTO items_sale VALUES(3, 2026-02-07, 'Хлеб', 
    25500, 30, 'Макдональдс', 'Вячеслав Савельевич Баштурмак')""")

    # Изменение данных в таблице
    cur.execute("UPDATE items_sale SET discount = 35 WHERE price BETWEEN 10000 AND 50000")



