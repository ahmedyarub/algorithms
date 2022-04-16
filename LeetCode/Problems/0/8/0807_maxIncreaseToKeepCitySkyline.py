class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        max_rows = [max(row) for row in grid]
        max_cols = [max(col) for col in zip(*grid)]

        return sum(min(max_rows[r], max_cols[c]) - val
                   for r, row in enumerate(grid)
                   for c, val in enumerate(row))
