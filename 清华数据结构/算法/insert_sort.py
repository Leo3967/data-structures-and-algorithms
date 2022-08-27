def insert_sort(li):
    for i in range(1, len(li)):  # i表示摸到的牌的下标
        temp = li[i]  # 摸到的牌
        j = i - 1  # j指的是手里的牌的最后一张
        while li[j] > temp and j >= 0:
            li[j+1] = li[j]
            j = j - 1
        li[j+1] = temp
    return li

li = [3, 2, 4, 1, 5, 6, 8, 7, 9]
li_new = insert_sort(li)
print(li_new)

