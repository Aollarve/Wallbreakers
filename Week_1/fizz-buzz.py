class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ret_arr = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                ret_arr.append("FizzBuzz")
            elif i%5 == 0:
                ret_arr.append("Buzz")
            elif i%3 == 0:
                ret_arr.append("Fizz")
            else:
                ret_arr.append(str(i))
        return ret_arr