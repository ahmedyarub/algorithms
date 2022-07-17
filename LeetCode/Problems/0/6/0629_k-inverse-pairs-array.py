class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [[0] * (k + 2) for _ in range(n + 2)]

        for i in range(1, n + 1):
            for j in range(k + 1):
                if not j:
                    dp[i][j] = 1
                else:
                    val = (dp[i - 1][j] - (dp[i - 1][j - i] if (j - i) >= 0 else 0))
                    dp[i][j] = (dp[i][j - 1] + val)

        return (dp[n][k] + 1000000007 - (dp[n][k - 1] if k > 0 else 0)) % 1000000007
