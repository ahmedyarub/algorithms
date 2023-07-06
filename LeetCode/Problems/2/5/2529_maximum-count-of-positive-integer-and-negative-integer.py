class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        return max(reduce(
            lambda cum, num: [cum[0] + (1 if num > 0 else 0), cum[1]] if num >= 0 else [cum[0], cum[1] + 1],
            nums,
            [0, 0]
        )
        )
