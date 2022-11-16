class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        def getDate(date):
            monthList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            return sum(monthList[: int(date[:2]) - 1]) + int(date[3:])

        return max(0, getDate(min(leaveAlice, leaveBob)) - getDate(max(arriveAlice, arriveBob)) + 1)