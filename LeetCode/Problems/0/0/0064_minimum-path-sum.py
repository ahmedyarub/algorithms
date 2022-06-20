class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[m - 1][n - 1] = 1
        for x in reversed(range(n)):
            for y in reversed(range(m)):
                nums = []
                if x + 1 < n:
                    nums.append(dp[y][x + 1])
                if y + 1 < m:
                    nums.append(dp[y + 1][x])

                dp[y][x] = grid[y][x] + min(nums, default=0)

        return dp[0][0]
