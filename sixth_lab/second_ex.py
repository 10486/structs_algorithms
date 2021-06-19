from typing import List


class Node:
    def __init__(self, value: int, parent=None):
        self.value = value
        self.parent: Node = parent
        self.left: Node = None
        self.right: Node = None


class SearchBinaryTree:
    def __init__(self, arr: List[int]):
        self.root: Node = Node(arr[0])
        for i in arr[1:]:
            self.append(i)

    def check(self):
        return self._check(self.root)

    @staticmethod
    def _check(node: Node):
        if node is None:
            return []
        tmp = [node.value]
        return SearchBinaryTree._check(node.left) + tmp + SearchBinaryTree._check(node.right)

    def append(self, value):
        self._append(self.root, value)

    @staticmethod
    def _append(node: Node, value: int):
        if node.value == value:
            return
        elif node.value > value:
            if node.left is None:
                node.left = Node(value, node)
            else:
                SearchBinaryTree._append(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value, node)
            else:
                SearchBinaryTree._append(node.right, value)

    def search(self, value):
        return self._search(self.root, value)

    @staticmethod
    def _search(node: Node, value: int):
        if node is None:
            return None

        if node.value == value:
            return node
        elif node.value > value:
            return SearchBinaryTree._search(node.left, value)
        else:
            return SearchBinaryTree._search(node.right, value)

    def delete(self, value: int):
        node = self.search(value)
        # проверка на наличие элемента
        if node is None:
            return None
        # когда эелемент - корень
        if node == self.root:
            tmp = node.right
            while tmp.left is not None:
                tmp = tmp.left
            if tmp == node.right:
                tmp.left = node.left
            else:
                tmp.parent.left = tmp.right
                tmp.left = node.left
                tmp.right = node.right
            tmp.parent = None
            self.root = tmp
        # когда нет дочерних элементов
        elif node.left is None and node.right is None:
            if node.parent.value > node.value:
                node.parent.left = None
            else:
                node.parent.right = None
        # когда только правый дочерний элемент
        elif node.left is None:
            if node.parent.value > node.value:
                node.parent.left = node.right
            else:
                node.parent.right = node.right
        # когда только левый дочерний элемент
        elif node.right is None:
            if node.parent.value > node.value:
                node.parent.left = node.left
            else:
                node.parent.right = node.left
        # когда оба дочерних элемента
        else:
            tmp = node.right
            while tmp.left is not None:
                tmp = tmp.left
            tmp.parent.left = tmp.right
            tmp.right = node.right
            tmp.left = node.left
            if node.parent.value > node.value:
                node.parent.left = tmp
            else:
                node.parent.right = tmp


def main(numbers, key):
    tree = SearchBinaryTree(numbers)
    tree.delete(key)
    return tree.check()
