class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev, shift, cnt = nums[0], 0, 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                cnt += 1
                if cnt > 2:
                    shift += 1
            else:
                cnt = 1

            nums[i - shift] = nums[i]

        return len(nums) - shift
