class Solution:
    def myAtoi(self, s: str) -> int:
        result, i, negative, positive = 0, 0, False, False

        while i < len(s) and s[i] == ' ':
            i += 1

        if i < len(s) and s[i] == '+':
            positive = True
            i += 1

        if i < len(s) and s[i] == '-':
            negative = True
            i += 1

        if positive and negative:
            return 0

        while i < len(s) and ord('9') >= ord(s[i]) >= ord('0'):
            result = result * 10 + ord(s[i]) - ord('0')
            i += 1

        if negative:
            result *= -1

        if result < pow(-2, 31):
            return pow(-2, 31)
        elif result > (pow(2, 31) - 1):
            return pow(2, 31) - 1
        else:
            return result
