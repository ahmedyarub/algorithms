class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result, left, right, cur_sum = float('-inf'), 0, 0, 0

        while right < len(nums):
            cur_sum += nums[right]

            while cur_sum < 0 and left < right:
                cur_sum -= nums[left]
                left += 1

            result = max(cur_sum, result)
            right += 1

            if cur_sum < 0:
                cur_sum = 0
                left = right

        return result
