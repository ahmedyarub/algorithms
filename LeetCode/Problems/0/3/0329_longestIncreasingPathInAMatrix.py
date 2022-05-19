class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def traverse(i: int, j: int, s: int) -> int:
            self.scores[i][j] = max(self.scores[i][j], s)

            return max([traverse(ni, nj, s + 1) for ni, nj in [(i, j - 1), (i - 1, j), (i, j + 1), (i + 1, j)]
                        if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[0])
                        and matrix[ni][nj] > matrix[i][j] and self.scores[ni][nj] < s + 1], default=s)

        self.scores = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        return max([traverse(r, c, 1) for r, c in [(i, j) for i in range(len(matrix)) for j in range(len(matrix[0]))]
                    if not self.scores[r][c]])
