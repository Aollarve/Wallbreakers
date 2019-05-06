class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        ret_arr = []
        for i in range(0, len(A)):
            if A[i] % 2 == 0:
                ret_arr = [A[i]] + ret_arr
            else:
                ret_arr.append(A[i])
        return ret_arr
                