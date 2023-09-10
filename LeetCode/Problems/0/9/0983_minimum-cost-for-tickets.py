class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        pass_days, travel_days = [1, 7, 30], set(days)

        @cache
        def dp(cur_day: int) -> int:
            if cur_day >= days[-1]:
                return 0

            if cur_day not in travel_days:
                return dp(cur_day + 1)

            return min([cost + dp(cur_day + pass_day) for cost, pass_day in zip(costs, pass_days)])

        return dp(0)
