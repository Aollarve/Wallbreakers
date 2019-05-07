class Solution:
    def titleToNumber(self, s: str) -> int:
        ret = 0
        p = 1
        for i in range(len(s)-1, -1, -1):
            ret += (ord(s[i])-64)*p
            p *= 26
        return ret