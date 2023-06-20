class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        left, right, found, mid = 0, len(intervals) - 1, False, 0
        while left <= right:
            mid = left + (right - left) // 2
            if min(newInterval[1], intervals[mid][1]) - max(newInterval[0], intervals[mid][0]) >= 0:
                if mid and min(newInterval[1], intervals[mid - 1][1]) - max(newInterval[0], intervals[mid - 1][0]) >= 0:
                    right = mid - 1
                else:
                    found = True
                    intervals[mid] = [min(intervals[mid][0], newInterval[0]), max(intervals[mid][1], newInterval[1])]
                    break
            else:
                if mid < len(intervals) - 1:
                    if intervals[mid][1] < newInterval[0] and intervals[mid + 1][0] > newInterval[1]:
                        return intervals[:mid + 1] + [newInterval] + intervals[mid + 1:]

                if intervals[mid][1] < newInterval[0]:
                    left = mid + 1
                else:
                    right = mid - 1

        if found:
            i = mid + 1
            while i < len(intervals):
                if intervals[mid][1] < intervals[i][0]:
                    break
                elif intervals[mid][1] <= intervals[i][1]:
                    intervals[mid][1] = intervals[i][1]

                i += 1

            return intervals[0:mid + 1] + (intervals[i:] if i < len(intervals) else [])
        else:
            if intervals[-1][1] < newInterval[0]:
                return intervals[:] + [newInterval]
            else:
                return [newInterval] + intervals[:]
