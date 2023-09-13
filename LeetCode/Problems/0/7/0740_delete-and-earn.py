class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = defaultdict(int)
        max_number = 0
        # Precompute how many points we gain from taking an element
        for num in nums:
            points[num] += num
            max_number = max(max_number, num)

        @cache
        def dp(num: int) -> int:
            if not num:
                return 0
            if num == 1:
                return points[1]

            return max(dp(num - 1), dp(num - 2) + points[num])

        return dp(max_number)
