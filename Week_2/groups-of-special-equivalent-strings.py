class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        ret_d = {}
        for i in A:
            string_1 = "".join(sorted(i[::2]))
            string_2 = "".join(sorted(i[1::2]))
            full_string = string_1 + string_2
            if full_string not in ret_d:
                ret_d[full_string] = 1
            else:
                ret_d[full_string] += 1
        return len(ret_d)