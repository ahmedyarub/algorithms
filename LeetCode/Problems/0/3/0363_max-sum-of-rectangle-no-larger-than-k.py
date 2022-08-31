from bisect import bisect_left, insort
from typing import List


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        res = float('-inf')

        for col in range(len(matrix[0])):
            row_sums = [0] * len(matrix)
            for r in range(col, len(matrix)):
                col_sums, col_sum = [0], 0
                for i in range(len(matrix)):
                    row_sums[i] += matrix[i][r]
                    col_sum += row_sums[i]
                    diff = col_sum - k
                    idx = bisect_left(col_sums, diff)
                    if idx < len(col_sums):
                        if col_sums[idx] == diff:
                            return k
                        else:
                            res = max(res, col_sum - col_sums[idx])
                    insort(col_sums, col_sum)
        return res


if __name__ == '__main__':
    print(Solution().maxSumSubmatrix([[5, -4, -3, 4],
                                      [-3, -4, 4, 5],
                                      [5, 1, 5, -4]], 8))
    print(Solution().maxSumSubmatrix([[2, 2, -1]], 0))
    print(Solution().maxSumSubmatrix([[1, 0, 1], [0, -2, 3]], 2))
    print(Solution().maxSumSubmatrix([[2, 2, -1]], 3))
