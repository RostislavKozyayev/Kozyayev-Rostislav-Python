# Приложение ТОРГОВАЯ ФИРМА для автоматизированного контроля продаж
# товаров торговой фирмы. БД должна содержать таблицу Продажа товаров со следующей
# структурой записи: Дата продажи, Товар, Сумма, Скидка, Филиал, Менеджер.

import sqlite3 as sq

# Список данных для таблицы
trcomp_data = [
    (1 , '2025-08-25', 'Агуша с яблоком', 12599, 15, 'Пятёрочка', 'Евгений Васильевич Костромской'),
    (2, '2008-10-12', 'Детские наручники', 1500, 5, 'Магнит', 'Наталья Эдуардовна Будапешт'),
    (3, '2026-02-07', 'БигМак', 25500, 30, 'Макдональдс', 'Вячеслав Савельевич Баштурмак'),
    (4, '2012-04-23', 'Монитор', 3599, 25, 'DNS', 'Виктор Михайлович Анатоль'),
    (5, '2025-05-31', 'Воппер', 4599, 10, 'БургерКинг', 'Дарья Дмитриевна Белая'),
    (6, '2024-06-27', 'Шариковая ручка', 199, None, 'ОфисКласс', 'Антонина Вячеславовна Григорян'),
    (7, '2023-04-23', 'Клубника', 2499, 50, 'Ашан', 'Ольга Петровна Ворошилова'),
    (8, '2020-08-28', 'Ананас', 349, 5, 'Азбука Вкуса', 'Владислав Борисович Гулиев'),
]

# Создание Базы Данных
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
                manager TEXT NOT NULL
                )""")

    # Добавление данных в таблицу
    cur.executemany("INSERT INTO items_sale VALUES(?, ?, ?, ?, ?, ?, ?)", trcomp_data)
    cur.execute("""INSERT INTO items_sale VALUES(9, '2022-01-26', 'Кока Кола 1л', 129, 10, 
                'Магнит', 'Григорий Никитович Абдулмакак')""")
    cur.execute("""INSERT INTO items_sale (s_id, sale_date, product, price, branch, manager) 
                VALUES(10, '2018-11-06', 'Арбуз', 549, 'Светофор', 'Абдулла Рахметович Атонасян')""")

    # Поиск данных в таблице
    print("\nПолученные данные:")
    cur.execute("SELECT * FROM items_sale WHERE s_id <= 5")
    cur.execute("SELECT product, price, discount FROM items_sale WHERE price BETWEEN 1000 AND 7000")
    cur.execute("SELECT * FROM items_sale WHERE product LIKE 'А%'")
    for result in cur:
        print(result)

    # Изменение данных в таблице
    cur.execute("UPDATE items_sale SET discount = 35 WHERE price BETWEEN 10000 AND 50000")
    cur.execute("UPDATE items_sale SET price = price - 2000 WHERE price > 10000")
    cur.execute("UPDATE items_sale SET discount = discount + 10 WHERE discount <= 15 OR price < 1000")

    # Удаление данных из таблицы
    cur.execute("DELETE FROM items_sale WHERE product LIKE 'К%'")
    cur.execute("DELETE FROM items_sale WHERE s_id = 1 OR price = 1500")
    cur.execute("DELETE FROM items_sale WHERE discount IS NULL")
