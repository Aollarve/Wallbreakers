class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        unique_cands = {}
        for i in candies:
            if i not in unique_cands:
                unique_cands[i] = 1
            else:
                unique_cands[i] += 1
        return min(len(unique_cands.keys()), len(candies)//2)