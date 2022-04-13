class Solution:
    def toHex(self, num: int) -> str:
        result = []

        if num < 0:
            num = 2 ** 31 - digit + 1

        while num:
            digit = num % 16

            result.append(chr((ord('a') + digit - 10) if digit > 9 else ord('0') + digit))

            num //= 16

        return "".join(result[::-1])
