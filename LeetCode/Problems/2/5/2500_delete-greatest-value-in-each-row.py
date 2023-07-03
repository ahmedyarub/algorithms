class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
            heapify(row)

        return sum([max([heappop(row) for row in grid]) for _ in range(len(grid[0]))])
