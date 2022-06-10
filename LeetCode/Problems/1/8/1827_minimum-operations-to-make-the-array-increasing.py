class Solution:
    def minOperations(self, nums: List[int]) -> int:
        result = 0

        for i in range(len(nums) - 1):
            diff = nums[i] - nums[i + 1] + 1
            if diff > 0:
                result += diff
                nums[i + 1] += diff

        return result
