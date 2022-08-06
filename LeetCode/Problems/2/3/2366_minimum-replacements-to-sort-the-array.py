class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        cnt, mn = 0, nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > mn:
                repl = ceil(nums[i] / mn)
            else:
                repl = 1

            cnt += repl - 1
            mn = nums[i] // repl

        return cnt
