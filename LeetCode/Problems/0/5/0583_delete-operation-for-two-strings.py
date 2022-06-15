class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = dict()

        def lcs(m: int, n: int) -> int:
            nonlocal word1, word2, memo
            if not (m and n):
                return 0

            if (m, n) in memo:
                return memo[(m, n)]

            if word1[m - 1] == word2[n - 1]:
                result = 1 + lcs(m - 1, n - 1)
            else:
                result = max(lcs(m, n - 1), lcs(m - 1, n))

            memo[(m, n)] = result

            return result

        return len(word1) + len(word2) - 2 * lcs(len(word1), len(word2))
