class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        leading = 1
        i = 1
        while(leading != 0):
            if i > len(digits):
                digits = [leading]+digits
                break
            num = digits[-i] 
            num = num+leading
            if num > 9:
                digits[-i] = 0
                leading = num-9
                i += 1
            else:
                digits[-i] = num
                leading = 0
        return digits