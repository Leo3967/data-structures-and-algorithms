def count_sort(li, max_count=100):
    count = [0 for _ in range(max_count+1)]
    for i in li:
        count[i] += 1
    li.clear()
    for idx, j in enumerate(count):
        for i in range(j):
            li.append(idx)
    return

import random
li = list(range(100))
random.shuffle(li)
count_sort(li, 100)
print(li)