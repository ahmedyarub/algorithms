class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def dp(i: int, j: int) -> int:
            if i > j:
                return 0
            elif i == j:
                return 1
            elif s[i] == s[j]:
                return dp(i + 1, j - 1) + 2
            else:
                return max(dp(i, j - 1), dp(i + 1, j))

        return dp(0, len(s) - 1)
