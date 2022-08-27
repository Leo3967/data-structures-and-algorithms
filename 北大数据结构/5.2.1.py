# -*- coding: UTF-8 -*-
# 整数转换为任意进制

def toStr(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n // base, base) + convertString[n % base]

print(toStr(1453,16))