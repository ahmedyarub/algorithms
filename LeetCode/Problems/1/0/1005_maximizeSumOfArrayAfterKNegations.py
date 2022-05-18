class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        for _ in range(k):
            heapreplace(nums, -nums[0])
        return sum(nums)
