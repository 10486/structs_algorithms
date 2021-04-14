class Stack:
    def __init__(self):
        self.__colletion = []

    def pop(self):
        return self.__colletion.pop()

    def append(self, item):
        self.__colletion.append(item)

    def peak(self):
        self.__colletion[-1]

    def __len__(self):
        return len(self.__colletion)


def main(arr):
    s = Stack()
    for i in arr:
        s.append(int(i))
    acc = 1
    count = len(s)
    for i in range(count):
        acc *= s.pop()
    return acc ** (1 / count)
