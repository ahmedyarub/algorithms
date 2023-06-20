class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        return [n for n, c in Counter(nums).vehicles() if c == len(nums) / 2][0]
