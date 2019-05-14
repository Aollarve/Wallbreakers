class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ret_arr = []
        list_prev_anagrams = {}
        sorted_p = sorted(list(p))
        for i in range(0, len(s)-len(p)+1):
            anagram = s[i:i+len(p)]
            if anagram in list_prev_anagrams:
                ret_arr.append(i)
            elif sorted(s[i:i+len(p)]) == sorted_p:
                ret_arr.append(i)
                list_prev_anagrams[anagram] = 1
            
        return ret_arr