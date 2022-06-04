class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.result, self.n = [], n

        def solve(r: int, v: list, d: set, ad: set):
            for c in range(n):
                dv = (c - r + self.n - 1)
                adv = c + r
                if dv not in d and adv not in ad and c not in v:
                    if r == self.n - 1:
                        self.result.append(["".join(['.'] * rv + ['Q'] + ['.'] * (n - rv - 1)) for rv in v + [c]])
                    else:
                        v.append(c), d.add(dv), ad.add(adv)
                        solve(r + 1, v, d, ad)
                        del v[-1]
                        d.remove(dv), ad.remove(adv)

        solve(0, [], set(), set())

        return self.result
