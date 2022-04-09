class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if not n:
            return False

        return n & (-n) == n
