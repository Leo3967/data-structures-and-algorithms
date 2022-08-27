def partition(li, left, right):
    temp = li[left]
    while left < right:
        # 从右边开始找
        while left < right and li[right] >= temp:  # 从右边找比temp小的数
            right -= 1  # 往左走一位

        li[left] = li[right]  # 将小的数进行移位

        # 再从左边找比temp大的数
        while left < right and li[left] <= temp:
            left += 1
        li[right] = li[left]

    li[left] = temp # 双指针碰头, elft = right

    return left

def quick_sort(data, left, right):
    if left < right: # 至少两个元素
        mid = partition(data, left, right)
        quick_sort(data, left, mid-1)
        quick_sort(data, mid+1, right)
    return data

li = [5, 7, 4, 6, 3, 1, 2, 9, 8]
sorted_l = quick_sort(li, 0, len(li)-1)

print(sorted_l)