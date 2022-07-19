class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k
        two, one = k, k ** 2

        for i in range(3, n + 1):
            cur = (k - 1) * (one + two)
            two = one
            one = cur

        return one
