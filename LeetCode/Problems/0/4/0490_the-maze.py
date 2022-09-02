class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        queue = [start]

        while queue:
            r, c = queue.pop()

            for dir in ([0, -1], [-1, 0], [0, 1], [1, 0]):
                nxt_r, nxt_c = r, c
                while 0 <= nxt_r <= len(maze) - 1 and 0 <= nxt_c <= len(maze[0]) - 1 and maze[nxt_r][nxt_c] != 1:
                    nxt_r += dir[0]
                    nxt_c += dir[1]

                nxt_r -= dir[0]
                nxt_c -= dir[1]

                if nxt_r == destination[0] and nxt_c == destination[1]:
                    return True
                elif maze[nxt_r][nxt_c] != -1:
                    queue.append([nxt_r, nxt_c])

            maze[r][c] = -1

        return False
