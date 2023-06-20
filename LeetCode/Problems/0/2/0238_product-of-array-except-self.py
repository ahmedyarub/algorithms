class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cnt_zeros = sum(1 for num in nums if not num)
        prod = reduce(lambda prev, v: prev * v, [num for num in nums if num != 0], 1)
        for i in range(len(nums)):
            if cnt_zeros > 1:
                nums[i] = 0
            elif cnt_zeros == 1:
                nums[i] = 0 if nums[i] else prod
            else:
                nums[i] = prod // nums[i]

        return nums
