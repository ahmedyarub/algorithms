class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate_matrix(m):
            return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]) - 1, -1, -1)]

        for i in range(4):
            if mat == target:
                return True

            target = rotate_matrix(target)

        return False
