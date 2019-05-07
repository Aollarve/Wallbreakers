class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) < 1:
            return ""
        else:
            prefix = strs[0]
            for i in range(1, len(strs)):
                temp_prefix = ""
                for e in range(0, min(len(prefix), len(strs[i]))):
                    if prefix[e] != strs[i][e]:
                        break
                    else:
                        temp_prefix += prefix[e]
                if temp_prefix == "":
                    return ""
                else:
                    prefix = temp_prefix
            return prefix