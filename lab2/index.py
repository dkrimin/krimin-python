print("Лабораторная работа №2\n")
print("Задача №1\n")
m = int(input("Введите m: "))
n = int(input("Введите n: "))
if (n < m):
    for i in range(n, m):
        print(i)
print("Задача №2 \n")
n = int(input("Введите n: "))
if n > 0:
    for i in range(n, n + 10):
        print(i)
print("Задача №3 \n")
n = int(input("Введите n: "))
if n < 0:
    print("Число не равно  больше 0 \n")
elif n > 0:
    print("Не равно или меньше 0 \n")
else:
    print("Число не имеет знака \n")


input("Press any key")
