class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        @cache
        def dfs(exp: str) -> List[int]:
            if exp.isdigit():
                return [int(exp)]

            res = []
            for i, c in enumerate(exp):
                if c in "+-*":
                    res.extend([eval(str(l) + c + str(r)) for l in dfs(exp[:i]) for r in dfs(exp[i + 1:])])

            return res

        return dfs(expression)
