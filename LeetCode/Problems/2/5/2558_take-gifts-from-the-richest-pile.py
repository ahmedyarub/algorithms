class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        result = [-1 * gift for gift in gifts]
        heapify(result)

        for _ in range(k):
            heappush(result, int(sqrt(heappop(result) * -1)) * -1)

        return -sum(result)
