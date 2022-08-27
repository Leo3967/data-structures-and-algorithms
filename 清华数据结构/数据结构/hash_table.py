from re import S
from tkinter.messagebox import NO


class LinkList:
    class Node:
        def __init__(self, item=None) -> None:
            self.item = item
            self.next = None

    class LinkListIterator:
        def __init__(self, node) -> None:
            self.node = node
        def __next__(self):
            if self.node:
                cur_node = self.node 
                self.node = cur_node.next
                return cur_node.item
            else:
                raise StopIteration
        def __iter__(self):
            return self

    def __init__(self, iterable=None) -> None:
        # iterable表示可迭代对象，比如列表
        self.head = None
        self.tail = None
        if iterable:
            self.extend(iterable)

    def append(self, obj):
        s = LinkList.Node(obj)
        if not self.head:
            self.head = s
            self.tail = s
        else:
            self.tail.next = s
            self.tail = s

    def extend(self, iterable):
        for obj in iterable:
            self.append(obj)

    def find(self, obj):
        for n in self:
            if n == obj:
                return True
        else:
            return False
    
    def __iter__(self):
        return self.LinkListIterator(self.head)
    
    def __repr__(self):
        return '<<' + ','.join(map(str, self))+'>>'

# 做一个类似于集合的结构
class HashTable:
    def __init__(self, size=101) -> None:
        self.size = size
        self.T = [LinkList() for _ in range(size)]

    def h(self, k):
        # 哈希函数
        return k % self.size
    
    def insert(self, k):
        i = self.h(k)
        if self.find(k):
            print('DUplicated Insert')
        else:
            self.T[i].append(k)

    def find(self, k):
        i = self.h(k)
        return self.T[i].find(k)

ht = HashTable()
for i in range(200):
    ht.insert(i)

print(ht.T)
print(ht.find(303))