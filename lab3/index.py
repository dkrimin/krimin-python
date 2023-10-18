import random
print("Лабораторная работа №3\n")
n = int(input("Введите начальное значение : "))
m = int(input("Введите конечное значение : "))
k = int(input("Введите размерность списка : "))
j = int(input("Введите число для поиска : "))
spisok = []
while len(spisok) < k:
    x = random.randint(n, m)
    if x not in spisok:
        spisok.append(x)

spisok.sort()
def bs(s, l, h, q):
    m  = (l + h)// 2
    if (l > h):
        return -1
    if s[m] == q:
        return m
    if s[m] < q:
        h = m - 1
        return bs(s, l, h, q)
    if s[m] > q:
        l = m + 1
        return bs(s, l, h, q)

right = k -1    
z = bs(spisok, 0, right, j)    
if z == -1:
    print("Число не найдено \n")
else:
    print("Объект находится под номером ", z)