class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)

        left_sum = 0
        for i, n in enumerate(nums):
            if left_sum == (s - left_sum - n):
                return i

            left_sum += n

        return -1
