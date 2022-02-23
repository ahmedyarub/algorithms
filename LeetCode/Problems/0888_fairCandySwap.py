class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sum_a, sum_b = sum(aliceSizes), sum(bobSizes)
        set_b = set(bobSizes)

        for a in aliceSizes:
            b = a + (sum_b - sum_a) / 2
            if b in set_b:
                return [a, b]
