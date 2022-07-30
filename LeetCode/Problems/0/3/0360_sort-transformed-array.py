from typing import List


class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def quadratic(x):
            return a * x * x + b * x + c

        n = len(nums)
        index = 0 if a < 0 else n - 1
        l, r, ans = 0, n - 1, [0] * n
        while l <= r:
            l_val, r_val = quadratic(nums[l]), quadratic(nums[r])
            if a >= 0:
                if l_val > r_val:
                    ans[index] = l_val
                    l += 1
                else:
                    ans[index] = r_val
                    r -= 1
                index -= 1
            else:
                if l_val > r_val:
                    ans[index] = r_val
                    r -= 1
                else:
                    ans[index] = l_val
                    l += 1
                index += 1
        return ans
