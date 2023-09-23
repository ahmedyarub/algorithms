class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        n = len(nums)
        broken = n if nums[-1] >= nums[0] else 0

        for i in range(n - 1, 0, -1):
            if nums[i] < nums[i - 1]:
                if broken:
                    return -1
                else:
                    broken = i

        return n - broken
