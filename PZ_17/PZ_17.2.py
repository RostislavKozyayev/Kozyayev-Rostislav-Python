# Разработать программу с применением пакета tk,
# взяв в качестве условия одну любую задачу из ПЗ № 2 – 9.

import tkinter as tk
from tkinter import messagebox

def extract_first_digit():
    try:
        number = int(entry.get())
        if 100 <= number <= 999:
            result = number // 100
            result_label.config(text=f'Первая цифра (сотни): {result}')
        else:
            messagebox.showerror("Ошибка", "Введите **трёхзначное** число!")
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите **целое** число!")

# Создание главного окна
root = tk.Tk()
root.title("Извлечение первой цифры")
root.geometry("400x200")
root.configure(bg="#ddeeff")

# Виджеты интерфейса
title = tk.Label(root, text="Введите трёхзначное число", font=("Arial", 14), bg="#ddeeff")
title.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 12), justify="center")
entry.pack(pady=5)

button = tk.Button(root, text="Получить первую цифру", command=extract_first_digit, bg="#3399ff", fg="white", font=("Arial", 12))
button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), bg="#ddeeff", fg="green")
result_label.pack(pady=5)

# Запуск приложения
root.mainloop()
