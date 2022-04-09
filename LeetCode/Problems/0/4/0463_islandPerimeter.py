class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count = 0
        w = len(grid[0])
        h = len(grid)
        for r in range(h):
            for c in range(w):
                if grid[r][c]:
                    count += (c == 0 or not grid[r][c - 1])
                    count += (r == 0 or not grid[r - 1][c])
                    count += (c == (w - 1) or not grid[r][c + 1])
                    count += (r == (h - 1) or not grid[r + 1][c])

        return count
