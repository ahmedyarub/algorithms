class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        directions, di, trow, tcol, row, col, cycle, cnt = [[0, 1], [1, 0], [0, -1], [-1, 0]], 0, \
                                                           len(matrix) // 2, len(matrix[0]) // 2, 0, -1, 0, 1

        while cnt <= len(matrix) * len(matrix[0]):
            nrow = row + directions[di][0]
            ncol = col + directions[di][1]

            if len(matrix) - cycle > nrow >= cycle and len(matrix[0]) - cycle > ncol >= cycle:
                if col == cycle and row - 1 == cycle and di == 3:
                    cycle += 1
                    di = 0
                    nrow = row
                    ncol = col + 1

                matrix[nrow][ncol] = cnt
                cnt += 1
                row, col = nrow, ncol
            else:
                di += 1

        return matrix
