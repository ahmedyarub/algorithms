from typing import List


class Solution:
    def minBuildTime(self, blocks: List[int], split: int) -> int:
        heapify(blocks)

        while len(blocks) > 1:
            _ = heapq.heappop(blocks)
            heappush(blocks, split + heapq.heappop(blocks))

        return heappop(blocks)
