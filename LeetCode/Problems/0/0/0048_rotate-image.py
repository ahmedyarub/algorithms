class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        for row in range(l // 2):
            for col in range(row, l - row - 1):
                matrix[row][col], \
                matrix[col][l - row - 1], \
                matrix[l - row - 1][l - col - 1], \
                matrix[l - col - 1][row] = \
                    matrix[l - col - 1][row], \
                    matrix[row][col], \
                    matrix[col][l - row - 1], \
                    matrix[l - row - 1][l - col - 1]
