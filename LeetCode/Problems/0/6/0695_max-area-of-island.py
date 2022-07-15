class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]:
                    queue, island = [(row, col)], 1
                    grid[row][col] = 0
                    while queue:
                        crow, ccol = queue.pop()
                        grid[crow][ccol] = 0

                        for orow, ocol in product([-1, 0, 1], repeat=2):
                            if not (orow and ocol):
                                nrow = crow + orow
                                ncol = ccol + ocol

                                if len(grid) > nrow >= 0 and len(grid[0]) > ncol >= 0 and grid[nrow][ncol]:
                                    queue.append((nrow, ncol))
                                    grid[nrow][ncol] = 0
                                    island += 1

                    result = max(result, island)

        return result
