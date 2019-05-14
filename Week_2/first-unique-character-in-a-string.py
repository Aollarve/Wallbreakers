class Solution:
    def firstUniqChar(self, s: str) -> int:
        repeating = {}
        non_repeating = {}
        for i in range(0, len(s)):
            if s[i] in non_repeating:
                non_repeating.pop(s[i])
                repeating[s[i]] = i
            elif s[i] not in repeating:
                non_repeating[s[i]] = i
    
        lowest = 9223372036854775807
        for key, val in non_repeating.items():
            if val < lowest:
                lowest = val
        if lowest == 9223372036854775807:
            return -1
        else:
            return lowest