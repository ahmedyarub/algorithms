class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        start, end, largest, result = 0, k - 1, 0, []

        while end < len(nums):
            if nums[start] > largest:
                largest = nums[start]
                result = nums[start:end + 1]

            start += 1
            end += 1

        return result
