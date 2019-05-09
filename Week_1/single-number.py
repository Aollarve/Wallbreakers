class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        ret = []
        for num in nums:
            if num in d:
                d.pop(num)
            else:
                d[num] = num
        return d.popitem()[1]