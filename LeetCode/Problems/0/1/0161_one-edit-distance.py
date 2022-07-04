class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) > 1:
            return False

        si, st, diff = 0, 0, False
        while si < len(s) or st < len(t):
            if si < len(s) and st < len(t) and s[si] == t[st]:
                si += 1
                st += 1
            else:
                if diff:
                    return False

                diff = True

                if len(s) >= len(t):
                    si += 1

                if len(t) >= len(s):
                    st += 1

        return diff
