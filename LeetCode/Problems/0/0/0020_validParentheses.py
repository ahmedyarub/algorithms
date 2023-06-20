class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = {'(', '[', '{'}
        close_open = {')': '(', ']': '[', '}': '{'}
        stck = []

        for c in s:
            if c in open_brackets:
                stck.append(c)
            elif not len(stck) or close_open[c] != stck.pop():
                return False

        return not len(stck)
