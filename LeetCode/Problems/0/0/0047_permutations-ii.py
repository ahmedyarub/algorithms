class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = set()

        def backtrack(start: int):
            nonlocal result
            if start == len(nums):
                result.add(tuple((nums)))
            else:
                for i in range(start, len(nums)):
                    if i != start and nums[i] == nums[start]:
                        continue
                    nums[i], nums[start] = nums[start], nums[i]
                    backtrack(start + 1)
                    nums[i], nums[start] = nums[start], nums[i]

        backtrack(0)
        return list(map(list, result))
