class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ret_set = set()
        for i in nums1:
            if i in nums2:
                ret_set.add(i)
        return list(ret_set)
        