class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        result = 0

        while start or goal:
            result += (start % 2) != (goal % 2)

            start //= 2
            goal //= 2

        return result
