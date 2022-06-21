class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        def traverse(nums: List[int], sz, combs):
            if not sz:
                result.append(combs)

            for i in range(len(nums)):
                traverse(nums[i + 1:], sz - 1, combs + [nums[i]])

        for k in range(len(nums)):
            traverse(nums, k + 1, [])

        return result
