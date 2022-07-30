class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        points = sorted(set(map(tuple, points)))
        return points == sorted((points[0][0] + points[-1][0] - x, y) for x, y in points)
