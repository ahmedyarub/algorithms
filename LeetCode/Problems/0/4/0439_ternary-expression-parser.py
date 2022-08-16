class Solution:
    def parseTernary(self, expression: str) -> str:
        i = 0

        def parse() -> str:
            nonlocal i
            cur, nxt = expression[i], (expression[i + 1] if i < (len(expression) - 1) else None)
            i += 2
            if nxt != '?':
                return cur

            a, b = parse(), parse()

            return a if cur == 'T' else b

        return parse()
