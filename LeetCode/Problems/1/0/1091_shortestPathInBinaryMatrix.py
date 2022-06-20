class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        h, w = len(grid), len(grid[0])
        if grid[0][0] or grid[w - 1][h - 1]:
            return -1

        queue, visited = [[0, 0, 1]], {(0, 0)}

        while queue:
            x, y, cur_l = queue.pop(0)

            if (x, y) == (w - 1, h - 1):
                return cur_l

            for ox, oy in [[-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0]]:
                cur_x, cur_y = x + ox, y + oy

                if 0 <= cur_x < w and 0 <= cur_y < h and not grid[cur_y][cur_x] and (cur_x, cur_y) not in visited:
                    queue.append([cur_x, cur_y, cur_l + 1])
                    visited.add((cur_x, cur_y))

        return -1
