class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ls, rs = 0, sum(nums)

        ans = []
        for x in nums:
            ls += x
            ans.append(abs(ls - rs))
            rs -= x
        return ans
