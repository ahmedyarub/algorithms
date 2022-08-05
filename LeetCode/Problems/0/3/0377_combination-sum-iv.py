class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()

        @cache
        def comb(target: int) -> int:
            nonlocal nums

            cnt = 0
            for num in nums:
                if target == num:
                    cnt += 1
                elif num < target:
                    cnt += comb(target - num)
                else:
                    break

            return cnt

        return comb(target)
