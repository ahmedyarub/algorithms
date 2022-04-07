class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        s, ms = 0, 0

        for n in nums:
            s += n
            ms = min(s, ms)

        return 1 - ms
