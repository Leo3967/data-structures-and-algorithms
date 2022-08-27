# -*- coding: UTF-8 -*-
# 十进制转换为N进制

from pythonds.basic.stack import Stack

def baseConverter(decNumber, base):
    digits = "0123456789ABCDEF"
    
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]
    return newString

print(baseConverter(25, 2))
print(baseConverter(250, 16))