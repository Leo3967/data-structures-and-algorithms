def selected_sort_simple(li):
    li_new = []
    for i in range(len(li)):
        min_val = min(li)
        li_new.append(min_val)
        li.remove(min_val)

    return li_new

# 优化-不创建新的列表：将每次的最小元素放在原列表的最前（或最后）
def select_sort(li):
    for i in range(len(li)-1):  # 无序区，i是第几趟，类似冒泡
        min_loc = i  # 无序区的第一个位置
        for j in range(i, len(li)):  # i可以改为i+1
            if li[j] < li[min_loc]:
                min_loc = j
        li[i], li[min_loc] = li[min_loc], li[i]
    return li
    
li = [3, 2, 4, 1, 5, 6, 8, 7, 9]
li_new = select_sort(li)
print(li_new)

