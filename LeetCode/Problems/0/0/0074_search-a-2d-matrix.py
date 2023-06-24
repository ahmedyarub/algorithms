class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = 0, 0

        while r < len(matrix) and c < len(matrix[0]):
            if matrix[r][c] == target:
                return True
            elif r == len(matrix) - 1 and c == len(matrix[0]) - 1:
                return False

            if r < len(matrix) - 1:
                if matrix[r + 1][c] <= target:
                    r += 1
                    continue

            if c < len(matrix[r]) - 1 and matrix[r][c + 1] <= target:
                c += 1
            else:
                return False

        return False
