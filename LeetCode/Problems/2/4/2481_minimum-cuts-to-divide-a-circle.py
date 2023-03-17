class Solution:
    def numberOfCuts(self, n: int) -> int:
        return n if n % 2 and n != 1 else n // 2
