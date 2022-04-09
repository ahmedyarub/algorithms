class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [stone * -1 for stone in stones]
        heapify(h)

        while len(h) > 1:
            heappush(h, (heappop(h) - heappop(h)))

        return h[0] * -1
