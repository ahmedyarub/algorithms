class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mn, mx, result = nums[0], nums[0], nums[0]

        for num in nums[1:]:
            mn, mx = min(num, mx * num, mn * num), max(num, mx * num, mn * num)
            result = max(mx, result)

        return result
