class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        to_col = 0
        for row in reversed(range(len(grid))):
            for col in reversed(range(to_col, len(grid[0]))):
                if grid[row][col] < 0:
                    count += 1
                else:
                    if col == len(grid[0]) - 1:
                        return count
                    to_col = col + 1

        return count
