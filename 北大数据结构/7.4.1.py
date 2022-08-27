# -*- coding: UTF-8 -*-
# 插入排序，时间复杂度是O（N^2）

def insertionSort(alist):
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position - 1] > currentvalue:
            alist[position] = alist[position-1]
            position = position - 1

        alist[position] = currentvalue

alist = [1,5,36,66,165,12,34]
insertionSort(alist)
print(alist)