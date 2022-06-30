class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        l = len(nums)
        if l % 2:
            med = nums[l // 2]
        else:
            med = (nums[l // 2 - 1] + nums[l // 2]) // 2

        return sum([abs(med - n) for n in nums])
