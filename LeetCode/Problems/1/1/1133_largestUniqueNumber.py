class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        return max([v for v,c in Counter(nums).items() if c == 1],)