class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = [int(digit) for digit in str(n)]

        s = 0
        product = 1

        for digit in digits:
            s += digit
            product *= digit

        return product - s
