class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dic = {}
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        new_dic = {}
        for i in t:
            if i not in dic:
                return i
            else:
                new_dic.setdefault(i, 0)
                new_dic[i] += 1
                if new_dic[i] > dic[i]:
                    return i