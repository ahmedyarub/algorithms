class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        left, right, result = 0, len(nums) - 1, 0

        while left <= right:
            if left == right:
                result += nums[left]
            else:
                result += int(str(nums[left]) + str(nums[right]))

            left, right = left + 1, right - 1

        return result
