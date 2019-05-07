class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        pow_of_two = 1
        while(pow_of_two<n):
            pow_of_two *= 2
        return pow_of_two == n