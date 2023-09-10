class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp, result = {}, 1

        for num in arr:
            dp[num] = dp.get(num - difference, 0) + 1
            result = max(result, dp[num])

        return result
