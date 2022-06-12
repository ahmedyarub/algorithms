class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        return sum([abs(se - st) for se, st in zip(sorted(seats), sorted(students))])
