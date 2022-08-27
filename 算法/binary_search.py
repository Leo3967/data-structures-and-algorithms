def binary_search(li, val):
    left = 0
    right = len(li) - 1
    while left <= right:  # 候选区有值
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] > val:  # 待查找的值在mid左侧
            right = mid - 1
        else:
            left = mid + 1
    else:
        return None

li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ind = binary_search(li, 4)
print(ind)