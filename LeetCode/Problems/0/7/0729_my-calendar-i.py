class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        pair = (start, end)
        i = bisect_right(self.calendar, pair)

        if (not i or self.calendar[i - 1][1] <= start) and \
                (i >= len(self.calendar) or self.calendar[i][0] >= end):
            self.calendar.insert(i, pair)
            return True
        else:
            return False
