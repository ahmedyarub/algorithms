class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)

        return sorted(nums) == list(range(1, n)) + [n - 1]
