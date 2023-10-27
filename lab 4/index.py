
h = {}
def hash(x):
    y =                 ''
    for i in x:
        y = y + str(ord(i))
    y =  int(y)%256
    return y



def insert():
    a = 0
    while a == 0:
        b = input('введите значение для добавления в таблицу или стоп для окончания добавлений')
        if b != 'стоп':
            c = []
            if h.get(hash(b)) == None:
                c.append(b)
                h[hash(b)] = c
            else:
                h.get(hash(b)).append(b)
        else:
            a = a + 1





def delete():
    a = 0
    while a == 0:
        b = input('введите значение, которое нужно удалить или стоп для завершения удалений.')
        if b != 'стоп':
            if h.get(hash(b)) == None:
                print('ключа для данного значения не найдено')
            else:
                if b in h.get(hash(b)):
                    h.get(hash(b)).remove(b)
                else:
                    print('такого значения не найдено')
        else:
            a = a + 1







def serch():
    a = 0
    while a == 0:
        b = input('введите значение, которое нужно найти или стоп для остановки поиска')
        if b != 'стоп':
            if h.get(hash(b)) == None:
                print('такое значение не найдено')
            else:
                if b in h.get(hash(b)):
                    print(b)
                else:
                    print('такое значение не найдено')
        else:
            a = a + 1





a = int(0)
while a == 0:
    b = input('введите 1 для добавления элементов к таблице, 2 для удаления элементов, 3 для поиска элемента по значению, 4 для вывода таблицы или любой другой символ для остановки программы.')
    if b == '1':
        insert()
    elif b == '2':
        delete()
    elif b == '3':
        serch()
    elif b == '4':
        print(h)
    else:
        a = a + 1