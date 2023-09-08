class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = defaultdict(lambda: 1)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                dp[j, nums[j] - nums[i]] = dp[i, nums[j] - nums[i]] + 1
        return max(dp.values())
