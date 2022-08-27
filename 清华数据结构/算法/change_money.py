def change_money(n, t):
    m = [0 for _ in range(len(t))]
    for i, money in enumerate(t):
        m[i] = n // money
        n = n % money
    return m, n

t = [100, 50, 20, 5, 1]
m = change_money(376, t)
print(m)