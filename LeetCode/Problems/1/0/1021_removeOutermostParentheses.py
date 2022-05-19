class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result, count = [], 0

        for c in s:
            if count and not (count == 1 and c == ')'):
                result.append(c)

            if c == '(':
                count += 1
            else:
                count -= 1

        return "".join(result)
