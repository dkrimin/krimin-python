class Node: 
    def __init__(self, data): 
        self.data = data
        self.left = self.right = None 
class Tree: 
    def __init__(self):
        self.root = None 
    def __find(self, node, parent, value): 
        if node is None:
            return None, parent, False 
        if value == node.data:
            return node, parent, True 
        if value < node.data: 
            if node.left: 
                return self.__find(node.left, node, value) 
        if value > node.data:
            if node.right:
                return self.__find(node.right, node, value) 
        return node, parent, False # если обойдя всё дерево нет вершины с значением введённым пользователем, выдаёт радителя вершины, в которой закончил обход и то, что вершина с введённым значением не найдена.
    def append(self, obj): 
        if self.root is None: 
            self.root = obj
            return obj 
        s, p, fl_find = self.__find(self.root, None, obj.data) 
        if not fl_find and s:
            if obj.data < s.data:
                s.left = obj 
            else:
                s.right = obj # иначе правой.
        return obj # получаем введённое значение
    def show_tree(self, node): 
        if node is None:
            return 
        self.show_tree(node.right) # вызываем метод отображения для правой ветви
        print(node.data) 
        self.show_tree(node.left) 
    def __del_leaf(self, s, p): 
        if p.left == s: 
            p.left = None 
        elif p.right == s:
            p.right = None 
    def __del_one_child(self, s, p): 
        if p.left == s: 
            if s.left is None: 
                p.left = s.right 
            elif s.right is None: 
                p.left = s.left 
        elif p.right == s:
            if s.left is None:
                p.right = s.right
            elif s.right is None:
                p.right = s.left 
    def __find_min(self, node, parent): 
        if node.left: # если вершина левая
            return self.__find_min(node.left, node) 
        return node, parent 
    def del_node(self, key): 
        s, p, fl_find = self.__find(self.root, None, key) 
        if not fl_find: # если __find говорит вершины нет, получаем None
            return None
        if s.left is None and s.right is None:
            self.__del_leaf(s, p) 
        elif s.left is None or s.right is None:
            self.__del_one_child(s, p) 
        else:
            sr, pr = self.__find_min(s.right, s)
            s.data = sr.data
            self.__del_one_child(sr, pr) 
t = Tree() 
def insert(): 
    c = int(0)
    e = [] 
    while c == 0: 
        d = input('введите значение, которое будет добавлено к дереву в виде числа или стоп для остановки добавлений')
        if d != 'стоп':
            e.append(d)
        elif d == 'стоп':
            for i in e:
                t.append(Node(int(i)))
            c = c + 1 
def delit(): 
    c = 0
    e = [] 
    while c == 0: 
        d = input('введите значение, которое будет удалено из дерева в виде числа или стоп для остановки удалений')
        if d != 'стоп':
            e.append(d) 
        elif d == 'стоп':
            for i in e:
                t.del_node(int(i))
            c = c + 1 
a = int(0)
while a == 0: 
    b = input('введите 1 для добавления элементов к дереву, 2 для удаления элементов, 3 для вывода дерева или любой другой символ для остановки программы.')
    if b == '1':
        insert() 
    elif b == '2':
        delit() 
    elif b == '3':
        t.show_tree(t.root) 
    else:
        a = a + 1