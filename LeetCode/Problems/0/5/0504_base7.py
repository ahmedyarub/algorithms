class Solution:
    def convertToBase7(self, num: int) -> str:
        result = 0
        sgn = -1 if num < 0 else 1
        num *= sgn
        digit = 0
        while num:
            result = result + (num % 7) * (10 ** digit)
            num //= 7
            digit += 1

        return str(result * sgn)
