class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        def count(k):
            if k == max(10 - n, 0):
                return 0
            return k * (1 + count(k - 1))

        if n == 0:
            return 1
        return 9 * count(9) + 10
