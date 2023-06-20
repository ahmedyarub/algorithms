class Solution(object):
    def search(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            cur = nums[mid]
            if cur == target:
                return mid
            elif cur > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1
