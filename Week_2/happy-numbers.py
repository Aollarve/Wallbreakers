class Solution:
    def isHappy(self, n: int) -> bool:
        l_nums = []
        while(n != 1):
            str_n = str(n)
            l_nums.append(str_n)
            n = 0
            for x in str_n:
                n += int(x)*int(x)
            if str(n) in l_nums:
                return False
            
        return True