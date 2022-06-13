class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        nums.sort()
        return all([nums[i + 1] - nums[i] == 1 for i in range(len(nums) - 1)])
