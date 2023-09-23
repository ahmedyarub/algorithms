class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        @cache
        def count_bits(n: int) -> int:
            return bin(n).count('1')

        return sum(num for i, num in enumerate(nums) if count_bits(i) == k)
