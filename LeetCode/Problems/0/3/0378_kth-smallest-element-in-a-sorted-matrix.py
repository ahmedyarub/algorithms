class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        hp = []

        for row in matrix:
            for v in row:
                heappush(hp, -1 * v)

                if len(hp) > k:
                    heappop(hp)

        return heappop(hp) * -1
