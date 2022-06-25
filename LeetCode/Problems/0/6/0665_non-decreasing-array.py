class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        modded, stack = False, [nums[0]]
        for i in range(1, len(nums)):
            if i == len(nums) - 1 and not modded:
                return True

            while stack and stack[-1] > nums[i]:
                if modded:
                    return False
                else:
                    if nums[i + 1] > nums[i - 1]:
                        nums[i] = stack[-1]
                    modded = True
                stack.pop()

            stack.append(nums[i])

        return True
