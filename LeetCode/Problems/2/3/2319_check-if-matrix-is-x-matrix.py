class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        return all(
            ((row == col or len(grid) - row - 1 == col) and grid[row][col])
            or not ((row == col or len(grid) - row - 1 == col) or grid[row][col])
            for row in range(len(grid)) for col in range(len(grid[0]))
        )
