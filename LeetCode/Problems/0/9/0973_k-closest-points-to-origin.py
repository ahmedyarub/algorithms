class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hp = []
        for i in range(k):
            heappush(hp, [-1 * sqrt(points[i][0] * points[i][0] + points[i][1] * points[i][1]), points[i]])

        for point in points[k:]:
            dist = sqrt(point[0] * point[0] + point[1] * point[1])
            if dist < hp[0][0] * -1:
                heapreplace(hp, [dist * -1, point])

        return [pair[1] for pair in hp]
