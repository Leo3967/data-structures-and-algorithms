def fractional_backpack(goods, w):
    m = [0 for _ in range(len(goods))]
    total_v = 0
    for i, (price, weight) in enumerate(goods):
        if w >= weight:
            m[i] = 1
            w -= weight
            total_v += price
        else:
            m[i] = w / weight
            w = 0
            total_v += price * m[i]
            break
    return m, total_v

goods = [(60, 10), (100, 20), (120, 30)]  # （商品价值，重量）
goods.sort(key=lambda x: x[0]/x[1],reverse=True)
w = 50
print(goods)
print(fractional_backpack(goods, w))