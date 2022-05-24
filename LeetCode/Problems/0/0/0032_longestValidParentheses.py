class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack, cur, result = [], 0, 0

        for c in s:
            if c == '(':
                cur += 1
                stack.append(cur)
            elif not stack:
                cur = 0
            else:
                stack.pop()
                cur += 1

            result = max(cur - (0 if not stack else stack[-1]), result)

        return max(cur - (0 if not stack else stack[-1]), result)
