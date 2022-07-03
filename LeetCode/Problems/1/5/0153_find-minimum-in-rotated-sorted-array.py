class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (right + left) // 2
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif nums[mid] > nums[mid + 1]:
                return nums[mid + 1]

            if nums[mid] < nums[left]:
                right = mid - 1
            else:
                left = mid + 1

        return nums[0]
