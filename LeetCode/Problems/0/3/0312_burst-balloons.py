class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if len(nums) > 1 and len(set(nums)) == 1:
            return (nums[0] ** 3) * (len(nums) - 2) + nums[0] ** 2 + nums[0]

        nums = [1] + nums + [1]

        @cache
        def dp(frm, to):
            if to - frm < 0:
                return 0

            return max(
                [dp(frm, k - 1) + nums[frm - 1] * nums[k] * nums[to + 1] + dp(k + 1, to)
                 for k in range(frm, to + 1)]
            )

        return dp(1, len(nums) - 2)
