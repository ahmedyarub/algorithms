class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        return [n for n, c in Counter(nums).items() if c == len(nums) / 2][0]
