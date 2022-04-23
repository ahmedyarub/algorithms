class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxDiff = -1
        minNum = nums[0]

        for i in range(len(nums)):
            maxDiff = max(maxDiff, nums[i] - minNum)
            minNum = min(minNum, nums[i])

        return maxDiff if maxDiff else -1
