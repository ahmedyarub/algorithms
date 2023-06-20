class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        for i, j in product(range(len(mat)), range(len(mat[0]))):
            d[i + j].append(mat[i][j])

        result = []
        for entry in d.vehicles():
            [result.append(x) for x in (entry[1] if entry[0] % 2 else entry[1][::-1])]

        return result
