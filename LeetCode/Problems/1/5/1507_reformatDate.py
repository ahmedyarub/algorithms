class Solution:
    def reformatDate(self, date: str) -> str:
        ms = {
            'Jan': "01",
            'Feb': "02",
            'Mar': "03",
            'Apr': "04",
            'May': "05",
            'Jun': "06",
            'Jul': "07",
            'Aug': "08",
            'Sep': "09",
            'Oct': "10",
            'Nov': "11",
            'Dec': "12"
        }

        day, month, year = date.split()

        day = day[0:len(day) - 2]
        if len(day) < 2:
            day = "0" + day

        return str(year) + "-" + ms[month] + "-" + day
