
def merge(li, low, mid, high):
    i = low  # 左指针，左边的有序列表
    j = mid + 1  # 右指针，右边的有序列表
    ltmp = []
    while i <= mid and j <= high:  # 左右有序列表都有数
        if li[i] < li[j]:
            ltmp.append(li[i])
            i += 1
        else:
            ltmp.append(li[j])
            j += 1
    # while执行完，双指针其中一个已经指向末尾
    while i <= mid:
        ltmp.append(li[i])
        i += 1
    while j <= high:
        ltmp.append(li[j])
        j += 1
    li[low:high+1] = ltmp
    return

def merge_sort(li, low, high):
    if low < high:  # 至少有两元素
        mid = (low + high) // 2
        merge_sort(li, low, mid)
        merge_sort(li, mid+1, high)
        merge(li, low, mid, high)
    return
import random
li = list(range(100))
random.shuffle(li)
merge_sort(li, 0, len(li)-1)
print(li)