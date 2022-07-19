class Solution:
    def numSquares(self, n: int) -> int:
        square_nums = [i ** 2 for i in range(1, int(sqrt(n)) + 1)]

        @cache
        def minNumSquares(k: int) -> int:
            if k in square_nums:
                return 1

            return min([minNumSquares(k - square) + 1 for square in square_nums if square < k], default=float('inf'))

        return minNumSquares(n)
