class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        indexes = []
        for c in range(len(mat[0])):
            for r in range(len(mat)):
                if len(indexes) == k:
                    break
                if not mat[r][c] and (not c or mat[r][c - 1]):
                    indexes.append(r)

        i = 0
        while len(indexes) < k:
            if mat[i][-1]:
                indexes.append(i)
            i += 1

        return indexes
