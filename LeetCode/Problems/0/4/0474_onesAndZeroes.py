class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        strs.sort(key=len)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for st in strs:
            zeros = st.count("0")
            ones = len(st) - zeros
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)

        return dp[m][n]
