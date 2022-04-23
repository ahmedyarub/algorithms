class Solution:
    def maxDepth(self, s: str) -> int:
        m, cur = 0, 0
        for c in s:
            if c == '(':
                cur += 1
                m = max(m, cur)
            elif c == ')':
                cur -= 1

        return m
