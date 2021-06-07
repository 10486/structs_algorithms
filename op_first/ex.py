class Node:
    def __init__(self, value: bool = False, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, item):
        if self.head is None:
            self.head = self.tail = Node(value=item)
        else:
            self.tail.next = Node(value=item)
            self.tail = self.tail.next

    def delete(self, ind):
        item = self[ind]
        if item == self.head:
            self.head = item.next
            self.head.prev = None
        elif item == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            item.prev.next = item.next
            item.next.prev = item.prev

    def find(self, item):
        for x, i in enumerate(self):
            if item == x.value:
                return i
        return -1

    def __getitem__(self, ind):
        item = self.head
        for _ in range(ind):
            item = item.next
        return item


def main():
    list = LinkedList()
    v = [1, 0, 0, 0, 1, 1, 0, 1]
    for i in v:
        list.append(i)
    while list.find(1) != -1:
        list.delete(list.find(1))
    while list.find(0) != -1:
        list.delete(0)
