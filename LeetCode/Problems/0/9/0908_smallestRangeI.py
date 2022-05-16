class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        mx, mn = max(nums), min(nums)
        diff, extension = mx - mn, 2 * k

        if diff <= extension:
            return 0
        else:
            return diff - extension
