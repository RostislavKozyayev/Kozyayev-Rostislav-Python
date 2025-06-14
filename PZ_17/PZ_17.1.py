# В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
# его в IDE PyCharm Community с применением пакета tk.
# Получить интерфейс максимально приближенный к оригиналу

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Step 3: Educational Details")
root.geometry("700x500")
root.configure(bg="#336699")
root.resizable(False, False)

style = ttk.Style()
style.theme_use("clam")
style.configure("TEntry", padding=5)
style.configure("TCombobox", padding=3)
style.configure("TSpinbox", padding=3)

frame = tk.LabelFrame(root, text="Registration Details", font=("Arial", 12, "bold"),
                      fg="white", bg="#336699", bd=1, relief="solid", labelanchor="nw")
frame.place(x=40, y=40, width=620, height=370)

label_right_x = 190  # Все надписи будут выровнены по правому краю относительно этой точки
entry_x = 200        # Все поля начинаются строго после надписей

# Университет
tk.Label(frame, text="University :", font=("Arial", 10), bg="#336699", fg="white")\
    .place(x=label_right_x - 80, y=20)  # Примерно 80px ширина текста
ttk.Entry(frame, width=45).place(x=entry_x, y=20)

# Институт
tk.Label(frame, text="Institute :", font=("Arial", 10), bg="#336699", fg="white")\
    .place(x=label_right_x - 72, y=60)
ttk.Entry(frame, width=45).place(x=entry_x, y=60)

# Branch
tk.Label(frame, text="Branch :", font=("Arial", 10), bg="#336699", fg="white")\
    .place(x=label_right_x - 58, y=100)
branch_combo = ttk.Combobox(frame, values=["-- select --", "CSE", "EEE", "ME"], width=20)
branch_combo.current(0)
branch_combo.place(x=entry_x, y=100)

# Degree
tk.Label(frame, text="Degree :", font=("Arial", 10), bg="#336699", fg="white")\
    .place(x=label_right_x - 60, y=140)
degree_combo = ttk.Combobox(frame, values=["-- select --", "B.Tech", "M.Tech", "PhD"], width=15)
degree_combo.current(0)
degree_combo.place(x=entry_x, y=140)

degree_status = tk.StringVar()
tk.Radiobutton(frame, text="Pursuing", variable=degree_status, value="Pursuing",
               bg="#336699", fg="white").place(x=330, y=140)
tk.Radiobutton(frame, text="Completed", variable=degree_status, value="Completed",
               bg="#336699", fg="white").place(x=405, y=140)

# CPI
tk.Label(frame, text="Avarage CPI :", font=("Arial", 10), bg="#336699", fg="white")\
    .place(x=label_right_x - 88, y=180)
ttk.Spinbox(frame, from_=0.0, to=10.0, increment=0.1, width=5).place(x=entry_x, y=180)

# Upto Th Semester
tk.Label(frame, text="Upto", font=("Arial", 10), bg="#336699", fg="white")\
    .place(x=255, y=180)
ttk.Spinbox(frame, from_=1, to=12, width=5).place(x=295, y=180)
tk.Label(frame, text="Th Semester", font=("Arial", 10), bg="#336699", fg="white")\
    .place(x=350, y=180)

# Experience
tk.Label(frame, text="Experience :", font=("Arial", 10), bg="#336699", fg="white")\
    .place(x=label_right_x - 85, y=220)
ttk.Spinbox(frame, from_=0, to=50, width=5).place(x=entry_x, y=220)
tk.Label(frame, text="Years", font=("Arial", 10), bg="#336699", fg="white")\
    .place(x=255, y=220)

# Website
tk.Label(frame, text="Your Website Or Blog :", font=("Arial", 10), bg="#336699", fg="white")\
    .place(x=label_right_x - 155, y=260)
website_entry = ttk.Entry(frame, width=45)
website_entry.insert(0, "http://")
website_entry.place(x=entry_x, y=260)

# Навигация
tk.Button(root, text="⯇", font=("Arial", 12, "bold"), bg="yellowgreen", fg="white", width=2, height=1)\
    .place(x=300, y=430)

tk.Label(root, text="Step 2", font=("Arial", 10, "bold"), bg="#336699", fg="white")\
    .place(x=340, y=434)

tk.Button(root, text="⯈", font=("Arial", 12, "bold"), bg="yellowgreen", fg="white", width=2, height=1)\
    .place(x=400, y=430)

root.mainloop()
