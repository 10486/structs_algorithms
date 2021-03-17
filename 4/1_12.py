text = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
class Hashtable:
    def __init__(self, size:int):
        self.__collection = [0 for x in range(size)]
    def append(self, key, item):
        hash = ord(key)
        if self.__collection[hash] == 0:
            self.__collection[hash] = [item, 1]
        else:
            if(self.__collection[hash][0] == key)
            self.__collection[hash][1] += 1
    def __str__(self):
        return "\n".join([f'{x[0]}:{x[1]}' for x in self.__collection if x != 0])
table = Hashtable()
for i in text:
    table.append(i)
print(table)
