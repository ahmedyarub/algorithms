class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        print(nums)
        while nums[0] != nums[nums[0]]:
            nums[nums[0]], nums[0] = nums[0], nums[nums[0]]
            print(nums)
        return nums[0]
