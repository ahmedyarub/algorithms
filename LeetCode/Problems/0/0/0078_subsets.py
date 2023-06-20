class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def traverse(start: int) -> List[List[int]]:
            nonlocal nums

            result = [[]]

            if start < len(nums):
                for i in range(start, len(nums)):
                    result.extend([[nums[i]] + nxt for nxt in traverse(i + 1)])

            return result

        return traverse(0)
