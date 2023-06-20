class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0

        def bfs(r: int, c: int):
            nonlocal result

            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and int(grid[r][c]) == 1:
                grid[r][c] = str(result * -1)
            else:
                return

            for offset in [[0, -1], [-1, 0], [0, 1], [1, 0]]:
                bfs(r + offset[0], c + offset[1])

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    result += 1
                    bfs(r, c)

        return result
