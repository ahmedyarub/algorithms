class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        w, r = 0, 0

        while r < len(nums) - 1:
            if nums[r]:
                nums[w] = nums[r]
                if nums[r] == nums[r + 1]:
                    nums[w] += nums[r]
                    nums[r + 1] = 0

                if w != r:
                    nums[r] = 0

                w += 1

            r += 1

        if not nums[w] and nums[r]:
            nums[w], nums[r] = nums[r], 0

        return nums
