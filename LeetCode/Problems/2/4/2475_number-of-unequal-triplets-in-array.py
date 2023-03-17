class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        c = Counter(nums)
        res = 0
        left, right = 0, len(nums)

        for freq in c.values():
            right -= freq
            res += left * freq * right
            left += freq

        return res
