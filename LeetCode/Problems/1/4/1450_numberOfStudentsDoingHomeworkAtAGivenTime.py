class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return sum(s <= queryTime for s in startTime) - sum(e < queryTime for e in endTime)
