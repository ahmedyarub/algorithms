class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n <= 1:
            return n
        ans = [0] * (n + 1)
        ans[1] = 1
        ln = (n + 1) // 2
        for i in range(1, ln):
            ans[i * 2] = ans[i]
            ans[(i * 2) + 1] = ans[i] + ans[i + 1]
        return max(ans)
