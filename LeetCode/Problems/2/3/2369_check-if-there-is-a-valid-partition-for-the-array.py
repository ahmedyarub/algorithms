class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        @cache
        def dp(i: int) -> bool:
            if i < 0:
                return True

            ans = False

            if i > 0 and nums[i] == nums[i - 1]:
                ans |= dp(i - 2)
            if i > 1 and nums[i] == nums[i - 1] == nums[i - 2]:
                ans |= dp(i - 3)
            if i > 1 and nums[i] == nums[i - 1] + 1 == nums[i - 2] + 2:
                ans |= dp(i - 3)

            return ans

        return dp(len(nums) - 1)
