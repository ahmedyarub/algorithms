class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals = sorted(intervals + [newInterval])

        i = 0
        while i < len(intervals) - 1:
            if intervals[i][0] <= intervals[i + 1][1] and intervals[i][1] >= intervals[i + 1][0]:
                intervals[i][0], intervals[i][1] = \
                    min(intervals[i][0], intervals[i + 1][0]), max(intervals[i][1], intervals[i + 1][1])
                del intervals[i + 1]
            else:
                i += 1
        return intervals
