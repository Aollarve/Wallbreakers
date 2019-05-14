class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        arr_s = []
        dic = {}
        count = 1
        for letter in s:
            if letter not in dic:
                dic[letter] = count
                count += 1
            arr_s.append(dic[letter])
        dic = {}
        count = 1
        arr_t = []
        for letter in t:
            if letter not in dic:
                dic[letter] = count
                count += 1
            arr_t.append(dic[letter])
        return arr_t == arr_s