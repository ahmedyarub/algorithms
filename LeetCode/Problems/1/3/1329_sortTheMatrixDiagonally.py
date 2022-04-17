class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        heaps = [[] for _ in range(len(mat) + len(mat[0]) - 1)]

        for ops in range(2):
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    if not ops:
                        heappush(heaps[len(mat) - i - 1 + j], mat[i][j])
                    else:
                        mat[i][j] = heappop(heaps[len(mat) - i - 1 + j])

        return mat
