class Solution:
    def binaryGap(self, N: int) -> int:
        if N == 0:
            return 0
        s = ""
        while(N):
            if N & 1 == 1:
                s = "1"+s
            else:
                s = "0"+s
            N = N >> 1
        seen = False
        temp = 0
        maxi = 0
        for i in s:
            if i == "1":
                temp += 1
                if temp > maxi and seen:
                    maxi = temp
                temp = 0
                seen = True
            elif seen:
                temp += 1
        return maxi