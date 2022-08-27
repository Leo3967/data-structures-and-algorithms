import random

def sift(li, low, high):  
    """堆的最后一个元素是high，堆顶也就是根节点是low"""
    # 假设节点的左右子树都是堆，但自身不是堆
    i = low    # i开始指向根节点
    j = 2 * i + 1  # i,j表示在调整时的上下两个点,j先看左孩子节点
    tmp = li[low]  # 把堆顶存起来

    while j <= high:  # 只要j位置没有越界
        if j + 1 <= high and li[j+1] > li[j]:  # 有右节点且比较大
            j += 1  # j指向右孩子节点
        if li[j] > tmp:
            li[i] = li[j]
            i = j  # 往下看一层
            j = 2 * i + 1
        else:  # tmp更大，将tmp放到i的位置上即可
            li[i] = tmp  # 将tmp放在某一级领导的位置上
            break
    else:
        li[i] = tmp  # i指向最后一层，j越界的情况
        # 此处的while else语句是必要的，否则while结束后会再执行一次tmp赋值
    return

def heap_sort(li):
    n = len(li)
    for i in range((n-2) // 2, -1, -1):
        # i代表了建堆的时候调整的部分的根的下标
        sift(li, i, n-1)  
        # 这里的high可以用最后一个元素代替，因为high只是用于判定j越界不越界的，如果某个节点没有下一层了，那自然越界了
    # 建堆完成

    # 开始挨个出数，把下来的和要替换的那个交换，为了节省内存
    for i in range(n-1, -1, -1):  # i一直指的是当前堆的最后一个位置
        # 先交换，再向下调整
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i-1)  # i-1是新的high
    return

import heapq  # q代表queue，优先队列
import random

li = list(range(100))
random.shuffle(li)
heapq.heapify(li)  # 建堆，小根堆
for i in range(len(li)):
    print(heapq.heappop(li), end=',')  # 往外弹出最小的数
