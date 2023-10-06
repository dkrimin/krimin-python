import random
print("Лабораторная работа №1\n")
m = int(input("Введите количество строк: "))
n = int(input("Введите количество столбцов: "))
matrix = []
for i in range(m):
    matrix.append([])
    for g in range(n):
        matrix[i].append(random.randint(0, 100))
for el in matrix:
    print(el)
        