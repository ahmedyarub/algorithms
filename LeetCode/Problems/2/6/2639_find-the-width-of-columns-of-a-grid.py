class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        return [len(str(max([grid[j][i] for j in range(len(grid))], key=lambda n: len(str(n)))))
                for i in range(len(grid[0]))]
