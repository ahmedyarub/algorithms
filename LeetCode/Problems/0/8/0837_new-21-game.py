class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        @cache
        def dp(points: int) -> float:
            if n < points:
                return 0

            if k <= points:
                return 1

            if points + 1 < k:
                return (1 + maxPts) / maxPts * dp(points + 1) - 1 / maxPts * dp(points + maxPts + 1)

            return 1 / maxPts * sum(dp(points + i) for i in range(1, maxPts + 1))

        return dp(0)
