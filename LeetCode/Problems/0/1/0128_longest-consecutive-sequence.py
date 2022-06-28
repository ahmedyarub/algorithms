class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st, result, cur = set(nums), 0, 0

        for n in st:
            if n - 1 not in st:
                cnt = 1
                while n + cnt in st:
                    cnt += 1

                result = max(result, cnt)

        return result
