class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        nums[::2], nums[1::2] = sorted(nums[::2]), sorted(nums[1::2], reverse=True)
        return nums
