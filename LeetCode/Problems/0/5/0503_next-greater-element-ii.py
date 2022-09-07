class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack, res, first_loop = [], [-1] * len(nums), True
        for _ in range(2):
            for i, num in enumerate(nums):
                while stack and nums[stack[-1]] < num:
                    res[stack.pop()] = num
                if first_loop:
                    stack.append(i)

        return res