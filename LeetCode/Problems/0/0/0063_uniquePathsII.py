class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        h, w = len(obstacleGrid), len(obstacleGrid[0])

        mem = [[0] * w for _ in range(h)]
        if not obstacleGrid[0][0]:
            mem[0][0] = 1

        for i in range(h):
            for j in range(w):
                if not obstacleGrid[i][j] and (i or j):
                    mem[i][j] = sum([mem[ni][nj] for ni, nj in [[i - 1, j], [i, j - 1]] if
                                     ni >= 0 and nj >= 0 and not obstacleGrid[ni][nj]])

        return mem[h - 1][w - 1]
