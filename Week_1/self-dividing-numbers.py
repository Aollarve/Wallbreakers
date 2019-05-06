class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ret_arr = []
        for i in range(left, right+1):
            string_rep = str(i)
            if '0' not in string_rep:
                allowed = True
                for e in string_rep:
                    if i % int(e) != 0:
                        allowed = False
                        break
                if allowed:
                    ret_arr.append(i)
        return ret_arr