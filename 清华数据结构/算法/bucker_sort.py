def bucket_sort(li, n=100, max_num=10000):
    buckets = [[] for _ in range(n)]  # 创建桶
    for var in li:
        bucket_idx = min(var // (max_num // n), n-1)  # 10000也放到最后一个桶
        buckets[bucket_idx].append(var)
        # 插入的时候顺便排序
        for j in range(len(buckets[bucket_idx])-1, 0, -1):
            if buckets[bucket_idx][j] < buckets[bucket_idx][j-1]:
                buckets[bucket_idx][j], buckets[bucket_idx][j-1] = buckets[bucket_idx][j-1], buckets[bucket_idx][j]
            else:
                break
    sorted_li = []
    for buc in buckets:
        sorted_li.extend(buc)
    return sorted_li

import random
li = list(range(100))
random.shuffle(li)
sorted_li = bucket_sort(li, 10, 100)
print(sorted_li)