class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum([v for v, c in Counter(nums).items() if c == 1])
