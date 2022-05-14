class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        if nums[0] > nums[1]:
            max1, max2 = 0, 1
        else:
            max1, max2 = 1, 0

        for i in range(2, len(nums)):
            if nums[i] > nums[max1]:
                max2, max1 = max1, i
            elif nums[i] > nums[max2]:
                max2 = i

        return max1 if nums[max2] * 2 <= nums[max1] else -1
