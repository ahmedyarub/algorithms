class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        if not nums or lower < nums[0]:
            nums = [lower - 1] + nums

        if upper > nums[0]:
            nums = nums + [upper + 1]

        result = []

        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1]
            if diff > 1:
                result.append(str(nums[i - 1] + 1) + (("->" + str(nums[i] - 1)) if diff > 2 else ""))

        return result
