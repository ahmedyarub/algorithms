class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def max_score(i: int, j: int) -> int:
            if i > j:
                return 0

            s1 = nums[i] + min(max_score(i + 1, j - 1), max_score(i + 2, j))
            s2 = nums[j] + min(max_score(i, j - 2), max_score(i + 1, j - 1))
            score = max(s1, s2)

            return score

        p1 = max_score(0, len(nums) - 1)
        return p1 >= (sum(nums) - p1)
