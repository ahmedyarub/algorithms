class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        return sum([mat[r][r] for r in range(len(mat))]) + sum(
            [mat[r][len(mat[0]) - r - 1] for r in range(len(mat))]) - (
                   mat[len(mat) // 2][len(mat) // 2] if len(mat) % 2 else 0)
