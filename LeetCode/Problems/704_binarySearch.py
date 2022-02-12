class Solution(object):
    def search(self, nums, target):
        if target < nums[0] or target > nums[-1]:
            return -1

        start = 0
        end = len(nums)

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return -1

