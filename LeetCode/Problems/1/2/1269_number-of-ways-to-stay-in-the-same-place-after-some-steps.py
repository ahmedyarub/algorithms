class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        @cache
        def dp(step, index):
            if step == 0:
                return 1 if index == 0 else 0

            if step < 0 or index < 0 or index >= arrLen:
                return 0

            ways = dp(step - 1, index)
            ways += dp(step - 1, index - 1)
            ways += dp(step - 1, index + 1)

            return ways % (10 ** 9 + 7)

        return dp(steps, 0)
