from typing import List


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


if __name__ == '__main__':
    obj = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
    print(obj.sumRegion(2, 1, 4, 3))
