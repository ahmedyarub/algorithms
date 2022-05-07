class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        area = 0
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    area += grid[i][j] * 4 + 2
                if i:
                    area -= min(grid[i][j], grid[i - 1][j]) * 2
                if j:
                    area -= min(grid[i][j], grid[i][j - 1]) * 2
        return area
