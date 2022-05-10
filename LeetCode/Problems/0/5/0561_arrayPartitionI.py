class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum([n for i, n in enumerate(sorted(nums)) if not i % 2])
