class Solution:
    def soupServings(self, n: int) -> float:
        n = (n + 24) // 25

        @cache
        def dp(i: int, j: int) -> float:
            if i <= 0 and j <= 0:
                return 0.5
            elif i <= 0:
                return 1.0
            elif j <= 0:
                return 0.0

            return 0.25 * (dp(i - 4, j) + dp(i - 3, j - 1) + dp(i - 2, j - 2) + dp(i - 1, j - 3))

        return dp(n, n)
