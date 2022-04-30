class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        diff = float('inf')
        result = -1

        for i, p in enumerate(points):
            if p[0] == x or p[1] == y:
                cur = abs(p[0] - x) + abs(p[1] - y)
                if cur < diff:
                    result = i
                    diff = cur

        return result
