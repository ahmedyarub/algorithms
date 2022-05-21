class Solution:
    def numberOfDays(self, year, month):
        monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        extraDay = month == 2 and (year % 100 and not year % 4) or not year % 400
        return monthDays[month - 1] + extraDay
