class Solution:
    def countTime(self, time: str) -> int:
        result = 1
        if time[3] == "?":
            result *= 6
        if time[4] == "?":
            result *= 10

        if time[0:2] == "??":
            result *= 24
        elif time[0] == "?" and time[1] != "?":
            result *= 2 if 3 < int(time[1]) < 10 else 3
        elif time[1] == "?" and time[0] != "?":
            result *= 10 if time[0] in ["0", "1"] else 4

        return result
