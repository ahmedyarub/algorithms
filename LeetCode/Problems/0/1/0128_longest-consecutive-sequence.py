class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st, result = set(nums), 0

        for num in nums:
            if num - 1 not in st:
                cur_streak, cur_num = 0, num
                while cur_num in st:
                    cur_streak += 1
                    cur_num += 1

                result = max(result, cur_streak)

        return result
