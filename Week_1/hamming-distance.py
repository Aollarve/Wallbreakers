class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        s_x = ""
        s_y = ""
        if x == 0:
            s_x = "0"
        if y == 0:
            s_y = "0"
        while(x):
            if x & 1 == 1:
                s_x = "1" + s_x
            else:
                s_x = "0" + s_x
            x = x >> 1
        while(y):
            if y & 1 == 1:
                s_y = "1" + s_y
            else:
                s_y = "0" + s_y
            y = y >> 1
        s_x = s_x.zfill(32)
        s_y = s_y.zfill(32)
        count = sum(1 for a, b in zip(s_x, s_y) if a != b)
        return count