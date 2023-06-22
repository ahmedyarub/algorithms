class Solution:
    def rob(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = max(nums[i] + (nums[i - 2] if i > 1 else 0), nums[i - 1])

        return nums[-1] if len(nums) > 2 else max(nums)
