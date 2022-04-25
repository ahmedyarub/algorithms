class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        rsets = [set() for _ in range(n)]
        csets = [set() for _ in range(n)]

        for i in range(n):
            for j in range(n):
                rsets[i].add(matrix[i][j])
                csets[j].add(matrix[i][j])

                if i == n - 1 and len(csets[j]) < n:
                    return False

            if len(rsets[i]) < n:
                return False

        return True
