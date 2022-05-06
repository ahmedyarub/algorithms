class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        return sum([sum([1 if n else 0 for n in row]) for row in grid]) + sum([max(row) for row in grid]) + sum([max(row) for row in zip(*grid)])