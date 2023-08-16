class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        ans, n = list(s), len(s)

        for i in range((n + 1) // 2):
            ans[i] = ans[n - i - 1] = min(ans[i], ans[n - i - 1])

        return ''.join(ans)
