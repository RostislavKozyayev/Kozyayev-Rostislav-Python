# Для каждого столбца матрицы с четным номером найти сумму ее элементов.

from random import randint

mat_lines, mat_columns = int(input("Введите кол-во строк матрицы: ")), int(input("Введите кол-во столбцов матрицы: "))
matrix = []
even_columns = list(filter(lambda j: (j + 1) % 2 == 0, range(mat_columns)))

# Формирование матрицы
for _ in range(mat_lines):
    matrix.append([randint(1, 100) for _ in range(mat_columns)])

# Вывод матрицы
print("\nПолученная матрица:")
for i in range(mat_lines):
    print(*[str(matrix[i][j]).ljust(3) for j in range(mat_columns)])
print()


# Поиск и суммирование чётных столбцов матрицы
for j in even_columns:
    print(f"Сумма чисел {j + 1} столбца равна:", sum(matrix[i][j] for i in range(mat_lines)))