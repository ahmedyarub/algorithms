class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = [False] * len(matrix), [False] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if not matrix[i][j]:
                    rows[i], cols[j] = True, True

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if rows[i] or cols[j]:
                    matrix[i][j] = 0
