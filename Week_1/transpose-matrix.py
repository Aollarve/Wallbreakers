class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        ret_mat = []
        for i in range(0, len(A)):
            for e in range(0, len(A[i])):
                if len(ret_mat) <= e:
                    ret_mat.append([A[i][e]])
                else:
                    ret_mat[e].append(A[i][e])
        return ret_mat