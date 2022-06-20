class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        directions, di, result, trow, tcol, row, col, cycle = [[0, 1], [1, 0], [0, -1], [-1, 0]], 0, [], \
                                                              len(matrix) // 2, len(matrix[0]) // 2, 0, -1, 0

        while len(result) != len(matrix) * len(matrix[0]):
            nrow = row + directions[di][0]
            ncol = col + directions[di][1]

            if len(matrix) - cycle > nrow >= cycle and len(matrix[0]) - cycle > ncol >= cycle:
                if col == cycle and row - 1 == cycle and di == 3:
                    cycle += 1
                    di = 0
                    nrow = row
                    ncol = col + 1

                result.append(matrix[nrow][ncol])
                row, col = nrow, ncol
            else:
                di += 1

        return result
