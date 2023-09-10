class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        result, prev, cur, zero = 0, 0, 0, False

        for num in nums:
            if num == 0:
                zero = True
                result = max(result, cur + prev)
                prev = cur
                cur = 0
            else:
                cur += 1

        return max(result, cur + prev - (0 if zero else 1))
