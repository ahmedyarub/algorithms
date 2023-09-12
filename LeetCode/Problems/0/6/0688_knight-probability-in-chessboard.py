class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(2, 1), (1, 2), (-2, 1), (-1, 2), (2, -1), (1, -2), (-2, -1), (-1, -2)]

        @cache
        def dp(r: int, c: int, rem: int) -> float:
            if not (0 <= r < n and 0 <= c < n):
                return 0

            if not rem:
                return 1

            return sum(dp(r + ro, c + co, rem - 1) for ro, co in moves) / 8

        return dp(row, column, k)
