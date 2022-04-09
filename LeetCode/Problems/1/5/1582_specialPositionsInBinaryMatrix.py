class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row_count = [sum(mat[i][n] for n in range(len(mat[0]))) for i in range(len(mat))]
        column_count = [sum(mat[m][j] for m in range(len(mat))) for j in range(len(mat[0]))]

        result = 0

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] and row_count[i] == 1 and column_count[j] == 1:
                    result += 1

        return result