class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    result += 1
                    queue = [(row, col)]

                    while queue:
                        crow, ccol = queue.pop()

                        for nrow, ncol in [(crow, ccol - 1), (crow - 1, ccol), (crow, ccol + 1), (crow + 1, ccol)]:
                            if 0 <= nrow < len(grid) and 0 <= ncol < len(grid[0]) and grid[nrow][ncol] == '1':
                                grid[nrow][ncol] = '2'
                                queue.append((nrow, ncol))
        return result
