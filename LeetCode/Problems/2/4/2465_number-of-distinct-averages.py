class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        return len({(nums[i] + nums[-1 * (i + 1)]) / 2 for i in range(len(nums) // 2)})
