class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        d, res = {(x, y): float('inf') if i else 0 for i, (x, y) in enumerate(points)}, 0
        while d:
            x, y = min(d, key=d.get)
            res += d.pop((x, y))
            for x1, y1 in d:
                d[(x1, y1)] = min(d[(x1, y1)], abs(x - x1) + abs(y - y1))
        return res
