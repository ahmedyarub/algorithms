class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)

        if s % 2:
            return False

        dp = [False] * (s // 2 + 1)
        dp[0] = True
        for num in nums:
            for j in range(s // 2, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[s // 2]
