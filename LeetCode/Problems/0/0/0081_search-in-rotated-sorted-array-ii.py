from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums)

        if nums[left] == nums[right - 1] and left != right and nums[left] != target:
            skip = nums[left]
            while nums[left] == skip and left < len(nums) - 1:
                left += 1
            while nums[right - 1] == skip and right > 0:
                right -= 1

        if left == right:
            return nums[left] == target

        while left < right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                if target < nums[0]:
                    left = mid + 1
                else:
                    right = mid
            else:
                right = mid

        return False


if __name__ == '__main__':
    print(Solution().search([1, 1, 3], 3))
