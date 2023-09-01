class Solution:
    def minBuildTime(self, blocks: List[int], split: int) -> int:
        heapify(blocks)

        while len(blocks) > 1:
            _ = heappop(blocks)
            heappush(blocks, split + heappop(blocks))

        return heappop(blocks)
