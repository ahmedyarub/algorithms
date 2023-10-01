class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        @cache
        def dp(i: int) -> int:
            if i == 0:
                return 1

            if nums[i] > nums[i - 1]:
                return dp(i - 1) + 1

            return 1

        return sum(dp(i) for i in range(1, len(nums))) + 1
