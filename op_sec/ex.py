import numpy as np


class SearchTree:
    root = None

    @staticmethod
    def _append(input_data, node):
        if node.data == input_data:
            return
        elif node.data > input_data:
            if node.left is None:
                node.left = Node(input_data, node)
            else:
                SearchTree._append(input_data, node.left)
        else:
            if node.right is None:
                node.right = Node(input_data, node)
            else:
                SearchTree._append(input_data, node.right)

    def append(self, input_data):
        if self.root is None:
            self.root = Node(input_data, None)
        else:
            SearchTree._append(input_data, self.root)

    @staticmethod
    def _find(input_data, node):
        if node.data == input_data:
            return node
        elif node.data > input_data:
            if node.left is None:
                return False
            else:
                return SearchTree._find(input_data, node.left)
        else:
            if node.right is None:
                return False
            else:
                return SearchTree._find(input_data, node.right)

    def find(self, input_data):
        return SearchTree._find(input_data, self.root)

    def list_of_levels(self):
        # не знаю зачем надо было обходить все дерево, но так написано в задании
        current_level = [self.root]
        levels = []
        check = current_level
        while check:
            levels.append(list(map(str, current_level)))
            next_level = list()
            for n in check:
                if n.left:
                    next_level.append(n.left)
                else:
                    next_level.append(None)
                if n.right:
                    next_level.append(n.right)
                else:
                    next_level.append(None)
            current_level = next_level
            check = [x for x in current_level if x is not None]
        return levels

    def delete_element(self, input_data):
        element = self.find(input_data)
        # проверка на наличие элемента
        if not element:
            return None
        # когда эелемент - корень
        if element == self.root:
            a = element.right
            while not (a.left is None):
                a = a.left
            if a == element.right:
                a.left = element.left
            else:
                a.parent.left = a.right
                a.left = element.left
                a.right = element.right
            a.parent = None
            self.root = a
        # когда нет дочерних элементов
        elif element.left is None and element.right is None:
            if element.parent.data > element.data:
                element.parent.left = None
            else:
                element.parent.right = None
        # когда только правый дочерний элемент
        elif element.left is None:
            if element.parent.data > element.data:
                element.parent.left = element.right
            else:
                element.parent.right = element.right
        # когда только левый дочерний элемент
        elif element.right is None:
            if element.parent.data > element.data:
                element.parent.left = element.left
            else:
                element.parent.right = element.left
        # когда оба дочерних элемента
        else:
            a = element.right
            while a.left is not None:
                a = a.left
            a.parent.left = a.right
            a.right = element.right
            a.left = element.left
            if element.parent.data > element.data:
                element.parent.left = a
            else:
                element.parent.right = a


# Узел дерева
class Node:
    parent = None
    left = None
    right = None
    data = None

    def __str__(self):
        return str(self.data)

    def __init__(self, data, parent):
        self.parent = parent
        self.data = data


def main(n: int):
    tree = SearchTree()
    arr = np.random.randint(-10, 10, size=10)
    for i in arr:
        tree.append(i)
    elements = ", ".join([x for x in tree.list_of_levels()[n] if x != 'None'])
    print(f"на уровне {n} имеются элементы - {elements} и они имеют по {n} предков")


main(3)
