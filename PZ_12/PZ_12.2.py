# Составить генератор (yield), который выводит из строки только цифры.

from string import digits

# Функция, результатом которой является генератор с цифрами из исходной строки
def only_nums_from_string(letters):
    for el in letters:
        if el in digits:
            yield el

# Ввод строки
symbols = str(input("Введите строку: "))

# Вывод полученного результата
print("Все цифры из строки:", *only_nums_from_string(symbols))
print("Класс результата функции:", type(only_nums_from_string(symbols)))