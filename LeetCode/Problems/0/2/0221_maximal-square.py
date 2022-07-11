class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        result = 0

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == '1':
                    matrix[row][col] = 1 if not (row and col) \
                        else min(matrix[row][col - 1], matrix[row - 1][col - 1], matrix[row - 1][col]) + 1

                    result = max(result, matrix[row][col])
                else:
                    matrix[row][col] = 0

        return result ** 2
