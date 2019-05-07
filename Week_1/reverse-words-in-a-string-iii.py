class Solution:
    def reverse(self, s):
        ret_s = ""
        for i in s:
            ret_s = i + ret_s
        return ret_s
    
    def reverseWords(self, s: str) -> str:
        list_of_words = s.split(" ")
        for i in range(0, len(list_of_words)):
            list_of_words[i] = self.reverse(list_of_words[i])
        return " ".join(list_of_words)