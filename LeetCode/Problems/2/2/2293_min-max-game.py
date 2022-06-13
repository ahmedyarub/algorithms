class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) > 1:
            nums = [(max(nums[i], nums[i + 1]) if i % 4 else min(nums[i], nums[i + 1])) for i in range(0, len(nums), 2)]

        return nums[0]
