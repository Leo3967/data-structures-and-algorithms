# -*- coding: UTF-8 -*-
# 冒泡排序

def bubbleSort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i]>alist[i + 1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]  # python支持直接交换

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)


# 选择排序,与冒泡排序相比，在每一趟只交换一次 但时间复杂度都是O（N^2）
def selectionSort(alist):
    for fillslot in range(len(alist) - 1, 0, -1):
        positionofMax = 0
        for location in range(1, fillslot + 1):
            if alist[location]>alist[positionofMax]:
                positionofMax = location

        temp = alist[fillslot]
        alist[fillslot] = alist[positionofMax]
        alist[positionofMax] = temp
