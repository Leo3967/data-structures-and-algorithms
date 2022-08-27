# 习题2
def searchMatrix(matrix, target):
    for line in matrix:
        if target in line:
            return True
    return False

def searchMatrix2(matrix, target):
    h = len(matrix)
    w = len(matrix[0])
    left = 0
    right = w * h - 1
    
    while left <= right:
        mid = (left + right) // 2
        i = mid // w; j = mid % w
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] > target:
            right = mid - 1
        else:
            left = mid + 1
    return False

a = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
print(searchMatrix(a, 12))