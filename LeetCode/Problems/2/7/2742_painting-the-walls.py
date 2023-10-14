class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        postfix_times = time.copy()

        for i in range(len(postfix_times) - 2, -1, -1):
            postfix_times[i] += postfix_times[i + 1]

        @cache
        def dp(index, time_painted):
            if index == len(cost):
                return 0 if time_painted >= 0 else float("inf")

            if time_painted >= len(cost) - index:
                return 0

            if time_painted + postfix_times[index] < 0:
                return float("inf")

            return min(
                dp(index + 1, time_painted - 1),
                cost[index] + dp(index + 1,
                                 time_painted + time[index]))

        return dp(0, 0)
