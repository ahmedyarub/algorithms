class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.result = []

        self.iterate(1, n - 1, '(')

        return self.result

    def iterate(self, open, remaining, st):
        if not remaining and not open:
            self.result.append(st)
            return

        if remaining:
            self.iterate(open + 1, remaining - 1, st + '(')

        if open:
            self.iterate(open - 1, remaining, st + ')')
