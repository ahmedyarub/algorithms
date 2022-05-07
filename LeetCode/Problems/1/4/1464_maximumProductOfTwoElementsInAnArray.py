class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        heap = []
        for i, n in enumerate(nums):
            heappush(heap, [-1 * n, i])

        return (heappop(heap)[0] + 1) * (heappop(heap)[0] + 1)
