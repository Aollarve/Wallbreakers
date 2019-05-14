class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dic = {}
        for i in range(0,len(nums)):
            dic[i+1] = 1
            
        ret_array = []
        for i in nums:
            try:
                dic.pop(i)
            except KeyError:
                ret_array.append(i)
        
        ret_array.append(dic.popitem()[0])
        return ret_array