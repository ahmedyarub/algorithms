class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                if cell:
                    top = matrix[i - 1][j] if i else float('inf')
                    left = matrix[i][j - 1] if j else float('inf')
                    matrix[i][j] = min(top, left) + 1

        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if cell := matrix[i][j]:
                    bottom = matrix[i + 1][j] if i < m - 1 else float('inf')
                    right = matrix[i][j + 1] if j < n - 1 else float('inf')
                    matrix[i][j] = min(cell, bottom + 1, right + 1)

        return matrix
