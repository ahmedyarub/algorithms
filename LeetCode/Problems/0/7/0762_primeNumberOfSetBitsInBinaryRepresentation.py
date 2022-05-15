class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        return sum([bin(n).count('1') in [2, 3, 5, 7, 11, 13, 17, 19] for n in range(left, right + 1)])
