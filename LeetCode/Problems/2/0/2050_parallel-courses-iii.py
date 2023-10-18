class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = [[] for _ in range(n)]

        for prev, nxt in relations:
            graph[prev - 1].append(nxt - 1)

        @cache
        def calculateTime(course: int) -> int:
            if not graph[course]:
                return time[course]

            max_prerequisite_time = 0
            for prereq in graph[course]:
                max_prerequisite_time = max(max_prerequisite_time, calculateTime(prereq))

            return max_prerequisite_time + time[course]

        overall_min_time = 0
        for course in range(n):
            overall_min_time = max(overall_min_time, calculateTime(course))

        return overall_min_time
