# 题目1
class Solution:
    def isAnagram(self, s, t):
        ss = list(s)
        tt = list(t)
        return sorted(ss) == sorted(tt)

class Solution:
    def isAnagram(self, s, t):
        # s，t里面字母的数量
        dict1 = {}
        dict2 = {}
        for ch in s:
            dict1[ch] = dict1.get(ch, 0) + 1
        for ch in t:
            dict2[ch] = dict2.get(ch, 0) + 1
        return dict1 == dict2
