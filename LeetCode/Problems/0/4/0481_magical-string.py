class Solution:
    def magicalString(self, n: int) -> int:
        s, i = ["1", "2", "2"], 2
        while len(s) < n:
            s += (["1"] if s[-1] == '2' else ["2"]) * int(s[i])
            i += 1

        return s[:n].count('1')
