class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        result = float('inf')
        nums.sort()
        for i in range(len(nums) - k + 1):
            result = min(result, nums[i + k - 1] - nums[i])

        return result if result != float('inf') else 0
