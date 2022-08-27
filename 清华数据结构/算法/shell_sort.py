def insert_sort_gap(li, gap):
    for i in range(gap, len(li)):  # i表示摸到的牌的下标
        temp = li[i]  # 摸到的牌
        j = i - gap  # j指的是手里的牌的最后一张
        while li[j] > temp and j >= 0:
            li[j+1] = li[j]
            j = j - gap
        li[j+gap] = temp
    return li

def shell_sort(li):
    d = len(li) // 2
    while d >= 1:
        insert_sort_gap(li, d)
        d = d // 2 

li = [3, 2, 4, 1, 5, 6, 8, 7, 9]
shell_sort(li)
print(li)
