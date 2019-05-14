class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        string = str.split(" ")
        if len(string) != len(pattern):
            return False
        dic = {}
        dic_2 = {}
        for i in range(0, len(pattern)):
            if pattern[i] in dic:
                if string[i] != dic[pattern[i]]: 
                    return False
            else:
                dic[pattern[i]] = string[i]
            
            if string[i] in dic_2:
                if dic_2[string[i]] != pattern[i]:
                    return False
            else:
                dic_2[string[i]] = pattern[i]
        return True