class Solution:
    def romanToInt(self, s: str) -> int:
        sym = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        result = 0
        last_digit = 0
        for c in reversed(s):
            digit = sym[c]

            if digit < last_digit:
                result -= digit
            else:
                result += digit
                last_digit = digit

        return result
