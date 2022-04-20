class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if not n:
            return 1

        return ((1 << (floor(log2(n)) + 1)) - 1) ^ n
