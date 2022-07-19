class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(nums)):
            j = i
            while j:
                if j % 2:
                    if j % 2 ^ nums[j] < nums[j - 1]:
                        nums[j], nums[j - 1] = nums[j - 1], nums[j]
                    else:
                        break
                else:
                    if nums[j] > nums[j - 1]:
                        nums[j], nums[j - 1] = nums[j - 1], nums[j]
                    else:
                        break

                j -= 1
