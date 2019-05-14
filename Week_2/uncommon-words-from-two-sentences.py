class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        full_list = A.split(" ") + B.split(" ")
        
        ret_list = []
        for i in full_list:
            if full_list.count(i) == 1:
                ret_list.append(i)
                
        return ret_list