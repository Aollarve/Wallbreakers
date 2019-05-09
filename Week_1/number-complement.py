class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0:
            return '1'
        s = ''
        while(num):
            if num & 1 == 1:
                s = s + "0"
            else:
                s = s + "1"
            num = num >> 1
        ret = 0
        for i in range(0, len(s)):
            ret += pow(2,i)*int(s[i])
        return ret