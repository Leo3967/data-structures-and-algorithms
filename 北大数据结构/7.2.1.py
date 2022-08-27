# -*- coding: UTF-8 -*-
# 二分查找

def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint + 1
            else:
                first = midpoint + 1
    return found

testlist = [1, 2, 8, 17, 27, 29, 42, 43, 100]
print(binarySearch(testlist, 43))
print(binarySearch(testlist, 13))