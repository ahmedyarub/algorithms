class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        pc, area = len(points), 0
        for i in range(pc - 2):
            for j in range(i + 1, pc - 1):
                for k in range(j + 1, pc):
                    cur_area = Area_Shoelace(points[i], points[j], points[k])
                    area = max(area, cur_area)

        return area


def Area_Shoelace(a, b, c):
    return abs(a[0] * b[1] + b[0] * c[1] + c[0] * a[1] - (a[0] * c[1] + c[0] * b[1] + b[0] * a[1])) / 2
