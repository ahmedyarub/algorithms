class Solution:
    def alternateDigitSum(self, n: int) -> int:
        sign, result = pow(-1, int(log(n + 0.1, 10))), 0

        while n:
            result += sign * (n % 10)
            sign *= -1
            n //= 10

        return result
