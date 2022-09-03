class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr: tuple, nms: List):
            if len(curr) >= 2 and curr[-1] < curr[-2]:
                return

            if len(curr) >= 2:
                result.add(curr[:])

            for i in range(len(nms)):
                backtrack(curr + (nms[i],), nms[i + 1:])

        result = set()
        backtrack((), nums)

        return list(result)
