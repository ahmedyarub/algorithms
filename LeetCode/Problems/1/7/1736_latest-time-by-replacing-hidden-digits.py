class Solution:
    def maximumTime(self, time: str) -> str:
        maxChar = lambda x: "23:59"[x] if time[0] in "2?" and time[1] in "0123?" else "19:59"[x]
        return "".join(t if t != "?" else maxChar(x) for x, t in enumerate(time))
