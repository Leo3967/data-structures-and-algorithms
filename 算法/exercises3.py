import enum


def twoSum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return sorted([i, j])
    return

def binary_search(li, left, right, val):
    while left <= right:  # 候选区有值
        mid = (left + right) // 2
        if li[mid][0] == val:
            return mid
        elif li[mid][0] > val:  # 待查找的值在mid左侧
            right = mid - 1
        else:
            left = mid + 1
    else:
        return None

# leetcode 167
def twoSum2(nums, target):
    n = len(nums)
    for i in range(n):
        a = nums[i]
        b = target - a
        if b >= a:
            j = binary_search(nums, i+1, n-1, b)
        else:
            j = binary_search(nums, 0, i-1, b)
        if j:
            break
    return  sorted([i+1, j+1])

def twoSum3(nums, target):
    new_nums = [[num, i] for i, num in enumerate(nums)]
    new_nums.sort(key=lambda x: x[0])
    n = len(new_nums)
    for i in range(n):
        a = new_nums[i][0]
        b = target - a
        if b >= a:
            j = binary_search(new_nums, i+1, n-1, b)
        else:
            j = binary_search(new_nums, 0, i-1, b)
        if j:
            break
    return  sorted([new_nums[i][1], new_nums[j][1]])

nums = [2, 7, 11, 15]
target = 17
print(twoSum3(nums, target))