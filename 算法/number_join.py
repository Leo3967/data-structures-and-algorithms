from errno import ESTALE
from functools import cmp_to_key

def xy_cmp(x, y):
    if x + y < y + x:
        return 1  # greater，进行交换
    elif x + y > y + x:
        return -1
    else:
        return 0

def number_join(li):
    li = list(map(str, li))
    li.sort(key=cmp_to_key(xy_cmp))
    print(li)
    return ''.join(li)

li = [32, 94, 128, 1286, 6, 71]
print(number_join(li))