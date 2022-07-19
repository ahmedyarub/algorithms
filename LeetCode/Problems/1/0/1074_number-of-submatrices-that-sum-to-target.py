class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                matrix[row][col] += (matrix[row][col - 1] if col > 0 else 0) \
                                    + (matrix[row - 1][col] if row > 0 else 0) \
                                    - (matrix[row - 1][col - 1] if row > 0 and col > 0 else 0)

        result = 0
        for frow in range(len(matrix)):
            for trow in range(frow, len(matrix)):
                h = defaultdict(int)
                h[0] = 1
                for col in range(len(matrix[0])):
                    area = matrix[trow][col] - (matrix[frow - 1][col] if frow > 0 else 0)

                    result += h[area - target]

                    h[area] += 1

        return result
