class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx, mn = nums[0], nums[0]
        result = mx

        for i in range(1, len(nums)):
            curr = nums[i]
            temp_max = max(curr, mx * curr, mn * curr)
            mn = min(curr, mx * curr, mn * curr)

            mx = temp_max

            result = max(mx, result)

        return result
