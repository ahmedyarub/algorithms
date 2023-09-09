class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]

        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                dp[j][i] = max(dp[j - 1][i - 1] + 1 if text1[i - 1] == text2[j - 1] else 0, dp[j - 1][i], dp[j][i - 1])

        return dp[-1][-1]
