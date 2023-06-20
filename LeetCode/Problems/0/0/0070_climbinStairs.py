class Solution:
    def climbStairs(self, n: int) -> int:
        prev_prev, prev, i = 0, 1, 0

        while i < n:
            prev_prev, prev = prev, prev + prev_prev
            i += 1

        return prev
