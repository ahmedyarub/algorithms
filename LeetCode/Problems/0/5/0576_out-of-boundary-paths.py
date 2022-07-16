class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @cache
        def traverse(m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
            if startRow < 0 or startRow == m or startColumn < 0 or startColumn == n:
                return 1
            elif not maxMove:
                return 0

            return sum(
                [traverse(m, n, maxMove - 1, startRow + ro, startColumn + co)
                 for ro, co in [[0, -1], [-1, 0], [0, 1], [1, 0]]])

        return traverse(m, n, maxMove, startRow, startColumn) % (10 ** 9 + 7)
