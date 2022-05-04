class Solution:
    def toHexspeak(self, num: str) -> str:
        n = int(num)

        result = []
        while n:
            digit = n % 16
            n //= 16

            if digit == 0:
                result.append('O')
            elif digit == 1:
                result.append('I')
            elif 16 > digit > 9:
                result.append(chr(digit - 10 + ord('A')))
            else:
                return "ERROR"

        return "".join(reversed(result))
