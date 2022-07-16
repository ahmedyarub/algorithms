class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        result = 0
        nums.sort()

        for i1 in range(len(nums) - 2):
            if nums[i1] > target and nums[i1 + 1] >= 0:
                break

            left, right = i1 + 1, len(nums) - 1
            while left < right:
                if nums[i1] + nums[left] + nums[right] < target:
                    result += right - left
                    left += 1
                else:
                    right -= 1

        return result
