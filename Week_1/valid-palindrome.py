class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_a = ""
        str_b = ""
        for i in s:
            if i.isalnum():
                str_a += i.lower()
                str_b = i.lower()+str_b
        return str_a == str_b