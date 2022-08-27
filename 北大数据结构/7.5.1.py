# -*- coding: UTF-8 -*-
# 谢尔排序 shell,以插入排序为基础
# 时间复杂度为n^(3/2)

def shellSort(alist):
    sublistcount = len(alist) // 2
    while sublistcount > 0:

        for startposition in range(sublistcount):
            gapInsertSort(alist, startposition, sublistcount)

        print("After increments of size", sublistcount, "The list is", alist)

        sublistcount = sublistcount // 2

def gapInsertSort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):

        currentvalue = alist[i]
        position = i

        while position > 0 and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currentvalue
    # print(alist)

alist = [1,5,36,66,165,12,34]
shellSort(alist)
print(alist)