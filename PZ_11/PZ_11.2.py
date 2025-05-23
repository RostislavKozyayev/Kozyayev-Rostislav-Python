# Из предложенного текстового файла (text18-14.txt) вывести на экран его содержимое, количество пробельных символов.
# Сформировать новый файл, в который поместить текст в стихотворной форме предварительно заменив символы третей строки их числовыми кодами.

with open("text18-14.txt", "rt", encoding="utf-8") as text18_14:

    # Считывание строк и пробелов
    text_li = text18_14.readlines()
    space_counter = 0

    for el in text_li:
        space_counter += el.count(" ")

    print("\nСодержимое файла text18-14.txt:\n", *text_li, "\n\nКоличество пробельных символов:\n", space_counter)

# Формирование нового файла с текстом старого, но с заменённой 3-ей строкой на числовые коды таблицы Unicode
with open("file3.txt", "wt", encoding="utf-8") as f3:
    third_line_codes = " ".join([str(ord(char)) for char in text_li[2]]) + "\n"
    text_li[2] = third_line_codes
    f3.writelines(text_li)