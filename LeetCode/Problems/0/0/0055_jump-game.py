class Solution:
    def canJump(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            if not nums[i]:
                found = False
                for j, n in enumerate(nums[:i]):
                    if j + n > i:
                        found = True
                        break

                if not found:
                    return False

        return True
