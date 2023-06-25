class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        queue, visited = [], set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '*':
                    queue.append([r, c, 0])
                    break

        while queue:
            r, c, d = queue.pop(0)
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] != 'X' and (r, c) not in visited:
                visited.add((r, c))
                if grid[r][c] == '#':
                    return d
                else:
                    queue.extend([[r + ro, c + co, d + 1] for ro, co in [[-1, 0], [0, 1], [1, 0], [0, -1]]])

        return -1
