class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        dp = [[0] * (k + 1) for _ in range(m + 1)]
        prefix = [[0] * (k + 1) for _ in range(m + 1)]
        prevDp = [[0] * (k + 1) for _ in range(m + 1)]
        prevPrefix = [[0] * (k + 1) for _ in range(m + 1)]
        MOD = 10 ** 9 + 7

        for num in range(1, m + 1):
            dp[num][1] = 1

        for i in range(1, n + 1):
            if i > 1:
                dp = [[0] * (k + 1) for _ in range(m + 1)]

            prefix = [[0] * (k + 1) for _ in range(m + 1)]
            for max_num in range(1, m + 1):
                for cost in range(1, k + 1):
                    ans = (max_num * prevDp[max_num][cost]) % MOD
                    ans = (ans + prevPrefix[max_num - 1][cost - 1]) % MOD

                    dp[max_num][cost] += ans
                    dp[max_num][cost] %= MOD

                    prefix[max_num][cost] = (prefix[max_num - 1][cost] + dp[max_num][cost]) % MOD

            prevDp = dp
            prevPrefix = prefix

        return prefix[m][k]
