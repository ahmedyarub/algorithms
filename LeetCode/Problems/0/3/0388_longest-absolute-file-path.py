class Solution:
    def lengthLongestPath(self, input: str) -> int:
        stack, result = [], 0

        for entry in input.splitlines():
            name, depth = entry.lstrip('\t'), entry.count("\t")

            while stack and stack[-1][1] >= depth:
                stack.pop()

            prefix = stack[-1][0] + '/' if stack else ""

            stack.append((prefix + name, depth))

            if stack and '.' in stack[-1][0]:
                result = max(result, len(stack[-1][0]))

        return result
