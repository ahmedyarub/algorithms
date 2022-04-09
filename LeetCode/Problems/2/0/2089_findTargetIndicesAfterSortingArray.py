class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        count = 0
        start = 0

        for _, n in enumerate(nums):
            if n < target:
                start += 1
            elif n == target:
                count += 1

        return [i for i in range(start, start + count)]
