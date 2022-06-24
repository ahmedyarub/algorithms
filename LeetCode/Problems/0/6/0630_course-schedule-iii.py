class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda course: course[1])
        heap, time = [], 0

        for duration, deadline in courses:
            if time + duration <= deadline:
                heapq.heappush(heap, -1 * duration)
                time += duration
            elif heap and heap[0] * -1 > duration:
                time += duration + heapq.heappop(heap)
                heapq.heappush(heap, -1 * duration)

        return len(heap)
