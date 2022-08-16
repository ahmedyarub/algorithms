class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        return [[max([max([grid[mrow][mcol] for mcol in range(col - 1, col + 2)]) for mrow in range(row - 1, row + 2)])
                 for col in range(1, len(grid[0]) - 1)] for row in range(1, len(grid) - 1)]
