# -*- coding: UTF-8 -*-
# 找零兑换问题
import time

def recMC(coinValueList, change):
    minCoins = change
    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMC(coinValueList, change-i)
            if numCoins < minCoins:
                minCoins = numCoins
    return minCoins

# 改进版
def recDC(coinValueList, change, knownResults):
    minCoins = change
    if change in coinValueList: #递归基本结束条件
        knownResults[change] = 1  #记录最优解
        return 1
    elif knownResults[change] > 0:
        return knownResults[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recDC(coinValueList, change - i, knownResults)
            if numCoins < minCoins:
                minCoins = numCoins
                knownResults[change] = minCoins
    return minCoins

'''
start = time.time()
print(recMC([1, 5, 10, 25], 63))
end = time.time()
print("递归解决找零问题耗时：", end - start)
'''
start = time.time()
memo = [0] * 64
print(recDC([1, 5, 10, 25], 63, memo))
end = time.time()
print("改进版递归解决找零问题耗时：", end - start)
print(memo)