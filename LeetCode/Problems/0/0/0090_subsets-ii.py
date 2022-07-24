class Solution:
    def subsetsWithDup(self, nums):
        if not nums:
            return []

        nums.sort()
        res, cur = [[]], []
        for i in range(len(nums)):
            cur = [item + [nums[i]] for item in (cur if i > 0 and nums[i] == nums[i - 1] else res)]
            res += cur

        return res
