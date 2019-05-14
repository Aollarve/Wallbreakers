class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        ret_count = 0
        for i in J:
            ret_count += S.count(i)
        return ret_count