class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        if start == destination:
            return 0

        queue, visited, res = deque([tuple(start + [0])]), {tuple(start): 0}, []

        while queue:
            prev_x, prev_y, prev_distance = queue.popleft()

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x, y, dist = prev_x, prev_y, prev_distance

                while 0 <= x + dx < len(maze) and 0 <= y + dy < len(maze[0]) and maze[x + dx][y + dy] == 0:
                    dist += 1
                    x += dx
                    y += dy

                if [x, y] == destination:
                    res.append(dist)
                    continue

                if ((x, y) in visited and visited[(x, y)] > dist) or ((x, y) not in visited):
                    visited[(x, y)] = dist
                    queue.append((x, y, dist))

        return min(res) if res else -1
