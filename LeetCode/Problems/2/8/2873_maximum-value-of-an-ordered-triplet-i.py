class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        pref = accumulate(nums, max)
        suff = list(accumulate(nums[::-1], max))[::-1]

        return max(0, *((j - i) * k for i, j, k in zip(nums[1:], pref, suff[2:])))
