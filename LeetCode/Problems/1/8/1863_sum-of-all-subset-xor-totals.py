class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        return sum(
            [sum([reduce(lambda s, n: s ^ n, comb) for comb in combinations(nums, l + 1)]) for l in range(len(nums))])
