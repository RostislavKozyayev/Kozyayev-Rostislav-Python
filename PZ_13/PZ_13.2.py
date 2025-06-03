# В двумерном списке найти минимальный элемент в предпоследнем столбце.

from random import randint

mat_lines, mat_columns = int(input("Введите кол-во строк матрицы: ")), int(input("Введите кол-во столбцов матрицы: "))
matrix = []

# Формирование двумерного списка
for _ in range(mat_lines):
    matrix.append([randint(1, 100) for _ in range(mat_columns)])

# Вывод матрицы
print("\nПолученная матрица:")
for i in range(mat_lines):
    for j in range(mat_columns):
        print(str(matrix[i][j]).ljust(3), end=" ")
    print()

# Поиск минимального элемента в предпоследнем столбце
sec_last_min_num = min([matrix[i][-2] for i in range(mat_lines)])
print("Минимальный элемент в предпоследнем столбце:", sec_last_min_num )