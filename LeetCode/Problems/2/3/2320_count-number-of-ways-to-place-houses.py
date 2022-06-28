class Solution:
    def countHousePlacements(self, n):
        a, b, mod = 1, 1, 10 ** 9 + 7
        for i in range(n):
            a, b = b, (a + b) % mod
        return b * b % mod
