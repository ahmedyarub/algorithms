class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        @cache
        def dp(i: int, j: int) -> int:
            if i == len(s1) and j == len(s2):
                return 0

            if i == len(s1):
                return ord(s2[j]) + dp(i, j + 1)

            if j == len(s2):
                return ord(s1[i]) + dp(i + 1, j)

            if s1[i] == s2[j]:
                return dp(i + 1, j + 1)

            return min(ord(s1[i]) + dp(i + 1, j), ord(s2[j]) + dp(i, j + 1))

        return dp(0, 0)
