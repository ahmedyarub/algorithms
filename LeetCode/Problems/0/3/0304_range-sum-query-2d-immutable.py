class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.sums = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        for r in range(len(matrix)):
            row = 0
            for c in range(len(matrix[0])):
                row += matrix[r][c]
                self.sums[r][c] = row + (self.sums[r - 1][c] if r else 0)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = self.sums[row2][col2]

        if row1:
            result -= self.sums[row1 - 1][col2]

        if col1:
            result -= self.sums[row2][col1 - 1]

        if col1 and row1:
            result += self.sums[row1 - 1][col1 - 1]

        return result
