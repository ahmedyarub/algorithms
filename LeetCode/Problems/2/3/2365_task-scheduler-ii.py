class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        days, mp = 0, {}

        for i, task in enumerate(tasks):
            days += 1
            if task in mp and days - mp[task] <= space:
                days += space - (days - mp[task] - 1)

            mp[task] = days

        return days
