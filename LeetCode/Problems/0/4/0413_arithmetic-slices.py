class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        result, start = 0, 1

        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                result += (i - start)
            else:
                start = i

        return result
