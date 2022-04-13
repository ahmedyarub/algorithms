class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:

        def f_date(date):  # calculates days passed since '1900-01-01'
            year0 = '1900'
            year1, month1, day1 = date.split('-')

            days = 0
            for y in range(int(year0), int(year1)):
                days += 365
                if y % 100 == 0:
                    if y % 400 == 0:
                        days += 1
                else:
                    if y % 4 == 0:
                        days += 1

            for m in range(int(month1)):
                if m in [1, 3, 5, 7, 8, 10, 12]:
                    days += 31
                if m in [4, 6, 9, 11]:
                    days += 30
                if m == 2:
                    days += 28
                    if int(year1) % 100 == 0:
                        if int(year1) % 400 == 0:
                            days += 1
                    else:
                        if int(year1) % 4 == 0:
                            days += 1
            days += int(day1)
            return days

        return abs(f_date(date1) - f_date(date2))
