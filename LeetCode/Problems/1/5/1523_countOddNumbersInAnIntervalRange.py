class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return low % 2 + (high - low + (0 if low % 2 else 1)) // 2
