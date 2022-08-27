# -*- coding: UTF-8 -*-
from pythonds.basic import Stack

class dog:
    def __init__(self):
        self.name = 'dog'
        self.height = '35'
        self.lenght = '36'

d = dog()
S = Stack()
S.push(d)

e = d
e.name = 'what'

f = S.pop()
print(f.name)