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

# Оформление стиля
style = ttk.Style()
style.configure("Rounded.TEntry", relief="flat", padding=5)
style.configure("Rounded.TSpinbox", relief="flat", padding=5)

frame = tk.LabelFrame(root, text="Registration Details", font=("Arial", 12, "bold"),
                      fg="white", bg="#336699", bd=2, relief="groove", labelanchor="nw")
frame.place(x=40, y=40, width=620, height=370)

# University
tk.Label(frame, text="University :", font=("Arial", 10), bg="#336699", fg="white")\
    .grid(row=0, column=0, padx=(20, 5), pady=10, sticky="e")
university_entry = ttk.Entry(frame, width=40)
university_entry.grid(row=0, column=1, columnspan=3, sticky="w")

# Institute
tk.Label(frame, text="Institute :", font=("Arial", 10), bg="#336699", fg="white")\
    .grid(row=1, column=0, padx=(20, 5), pady=10, sticky="e")
institute_entry = ttk.Entry(frame, width=40)
institute_entry.grid(row=1, column=1, columnspan=3, sticky="w")

# Branch
tk.Label(frame, text="Branch :", font=("Arial", 10), bg="#336699", fg="white")\
    .grid(row=2, column=0, padx=(20, 5), pady=10, sticky="e")
branch_combo = ttk.Combobox(frame, width=17, values=["-- select --", "CSE", "EEE", "ME"])
branch_combo.current(0)
branch_combo.grid(row=2, column=1, sticky="w")

# Degree
tk.Label(frame, text="Degree :", font=("Arial", 10), bg="#336699", fg="white")\
    .grid(row=3, column=0, padx=(20, 5), pady=10, sticky="e")
degree_combo = ttk.Combobox(frame, width=10, values=["-- select --", "B.Tech", "M.Tech", "PhD"])
degree_combo.current(0)
degree_combo.grid(row=3, column=1, sticky="w")

degree_status = tk.StringVar()
tk.Radiobutton(frame, text="Pursuing", variable=degree_status, value="Pursuing", bg="#336699", fg="white")\
    .grid(row=3, column=2, sticky="w", padx=(0, 2))
tk.Radiobutton(frame, text="Completed", variable=degree_status, value="Completed", bg="#336699", fg="white")\
    .grid(row=3, column=3, sticky="w")

# CPI and "Upto Th Semester"
tk.Label(frame, text="Average CPI :", font=("Arial", 10), bg="#336699", fg="white")\
    .grid(row=4, column=0, padx=(20, 5), pady=10, sticky="e")
cpi_spin = ttk.Spinbox(frame, from_=0.0, to=10.0, increment=0.1, width=5)
cpi_spin.grid(row=4, column=1, sticky="w")

# Frame for Upto Th Semester
semester_frame = tk.Frame(frame, bg="#336699")
semester_frame.grid(row=4, column=2, columnspan=2, sticky="w")

tk.Label(semester_frame, text="Upto", font=("Arial", 10), bg="#336699", fg="white")\
    .grid(row=0, column=0, sticky="e", padx=(0, 2))
semester_spin = ttk.Spinbox(semester_frame, from_=1, to=12, width=5)
semester_spin.grid(row=0, column=1, sticky="w")
tk.Label(semester_frame, text="Th Semester", font=("Arial", 10), bg="#336699", fg="white")\
    .grid(row=0, column=2, sticky="w", padx=(5, 0))

# Experience + Years
tk.Label(frame, text="Experience :", font=("Arial", 10), bg="#336699", fg="white")\
    .grid(row=5, column=0, padx=(20, 5), pady=10, sticky="e")
exp_spin = ttk.Spinbox(frame, from_=0, to=50, width=5)
exp_spin.grid(row=5, column=1, sticky="w")

exp_frame = tk.Frame(frame, bg="#336699")
exp_frame.grid(row=5, column=2, columnspan=2, sticky="w")
tk.Label(exp_frame, text="Years", font=("Arial", 10), bg="#336699", fg="white")\
    .grid(row=0, column=0, padx=(5, 0), sticky="w")

# Website
tk.Label(frame, text="Your Website Or Blog :", font=("Arial", 10), bg="#336699", fg="white")\
    .grid(row=6, column=0, padx=(20, 5), pady=10, sticky="e")
website_entry = ttk.Entry(frame, width=40)
website_entry.insert(0, "http://")
website_entry.grid(row=6, column=1, columnspan=3, sticky="w")

# Navigation buttons
tk.Button(root, text="⯇", font=("Arial", 10, "bold"), bg="yellowgreen", fg="white", width=3).place(x=300, y=430)
tk.Label(root, text="Step 2", font=("Arial", 10, "bold"), bg="#336699", fg="white").place(x=340, y=433)
tk.Button(root, text="⯈", font=("Arial", 10, "bold"), bg="yellowgreen", fg="white", width=3).place(x=400, y=430)

root.mainloop()
