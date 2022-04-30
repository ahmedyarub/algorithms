class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if c * r != len(mat) * len(mat[0]):
            return mat

        result = [[None] * c for _ in range(r)]

        ri = ci = 0
        for row in mat:
            for n in row:
                result[ri][ci] = n
                ci += 1
                if ci == c:
                    ci = 0
                    ri += 1

        return result
