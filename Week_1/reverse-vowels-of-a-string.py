class Solution:
    def reverseVowels(self, s: str) -> str:
        list_to_return = []
        list_of_vowels = []
        vowels = ['a','e','i','o','u']
        for i in s:
            if i.lower() in vowels:
                list_to_return.append("")
                list_of_vowels = [i] + list_of_vowels
            else:
                list_to_return.append(i)
        for i in range(0, len(list_to_return)):
            if list_to_return[i] == "":
                list_to_return[i] = list_of_vowels.pop(0)
        return "".join(list_to_return)