class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        return sum([abs(comb[1] - comb[0]) == k for comb in combinations(nums, 2)])
