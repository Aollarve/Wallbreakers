class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        ret_mat = []
        for i in range(0, len(A)):
            ret_mat.append([])
            for e in range(0, len(A[i])):
                if A[i][e] == 1:
                    ret_mat[i] = [0] + ret_mat[i]
                else:
                    ret_mat[i] = [1] + ret_mat[i]
        return ret_mat