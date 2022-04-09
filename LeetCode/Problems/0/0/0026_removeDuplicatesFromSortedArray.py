class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        read_index = 1
        writer_index = 1

        for read_index in range(1, len(nums)):
            if nums[read_index] != nums[read_index - 1]:
                nums[writer_index] = nums[read_index]
                writer_index += 1

        return writer_index