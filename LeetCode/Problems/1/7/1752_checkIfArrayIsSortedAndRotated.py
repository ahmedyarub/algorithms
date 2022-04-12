class Solution:
    def check(self, nums: List[int]) -> bool:
        cnt = 0

        for i in range(len(nums)):
            if nums[i - 1] > nums[i]:
                cnt += 1

        return cnt <= 1
