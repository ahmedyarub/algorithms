class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        left, right, first = 0, len(nums), -1
        while left <= right:
            mid = (left + right) // 2

            if mid == len(nums):
                break

            if nums[mid] == target:
                if first == -1:
                    if mid == 0 or nums[mid] > nums[mid - 1]:
                        first = mid
                        continue
                elif mid == len(nums) - 1 or nums[mid] < nums[mid + 1]:
                    return [first, mid]

            if first == -1:
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] == target:
                    right = len(nums)
                    if left < mid:
                        left = mid
                    else:
                        left = mid + 1
                else:
                    left = mid + 1

        return [-1, -1]
