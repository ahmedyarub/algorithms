class Solution:
    def sumBase(self, n: int, k: int) -> int:
        result = 0

        while n:
            n, rem = divmod(n, k)
            result += rem

        return result