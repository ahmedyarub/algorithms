class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        def compress_matrix(matrix: List[List[int]]) -> List[List[int]]:
            return [[col for col in range(len(matrix[0])) if matrix[row][col]]
                    for row in range(len(matrix))]

        m1 = compress_matrix(mat1)
        m2 = compress_matrix(mat2)

        ans = [[0] * len(mat2[0]) for _ in range(len(mat1))]

        for row1 in range(len(mat1)):
            for col1 in m1[row1]:
                for col2 in m2[col1]:
                    ans[row1][col2] += mat1[row1][col1] * mat2[col1][col2]

        return ans
