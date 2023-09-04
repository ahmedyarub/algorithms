class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        s, mx = sum(nums), 0
        for i in range(len(nums), 0, -1):
            mx = max(mx, ceil(s / i))
            s -= nums[i - 1]

        return mx
