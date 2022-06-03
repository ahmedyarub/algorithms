from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            x = len(nums) - mid

            if nums[mid] >= x:
                if mid == 0 or nums[mid - 1] < x:
                    return x
                else:
                    right = mid - 1
            else:
                left = mid + 1

        return -1


if __name__ == '__main__':
    print(Solution().specialArray([3, 6, 7, 7, 0]))
