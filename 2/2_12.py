class Stack:
    def __init__(self):
        self.__colletion = []
    def pop(self):
        return self.__colletion.pop()
    def append(self,item):
        self.__colletion.append(item)
    def peak(self):
        self.__colletion[-1]
    def __len__(self):
        return len(self.__colletion)

def main(filename:str):
    s = Stack()
    with open(filename, 'r') as f:
        for line in f.readlines():
            for i in line.split():
                s.append(int(i))
            acc = 1
            count = len(s)
            for i in range(count):
                acc *= s.pop()
            print(acc**(1/count))
