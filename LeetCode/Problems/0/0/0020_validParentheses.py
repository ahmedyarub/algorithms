class Solution:
    def isValid(self, s: str) -> bool:
        m = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        stack = []

        for c in s:
            if c in m:
                stack.append(c)
            else:
                if not stack or m[stack.pop()] != c:
                    return False

        return not stack
