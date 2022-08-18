class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()

        result, prev_inter = len(points), points[0]

        for pi in range(1, len(points)):
            if points[pi][0] <= prev_inter[1]:
                prev_inter = [points[pi][0], min(prev_inter[1], points[pi][1])]
                result -= 1
            else:
                prev_inter = points[pi]

        return result
