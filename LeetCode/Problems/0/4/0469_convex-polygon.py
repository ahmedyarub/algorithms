class Solution:
    def isConvex(self, points: List[List[int]]) -> bool:
        points.append(points[0])
        points.append(points[1])
        s = set()
        for i in range(len(points) - 2):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]
            x3, y3 = points[i + 2]
            z = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
            if z != 0:
                s.add(z > 0)
        return len(s) == 1
