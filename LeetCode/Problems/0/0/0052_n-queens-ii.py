class Solution:
    def totalNQueens(self, n: int) -> int:
        result = 0

        def solve(r: int, v: list, d: set, ad: set):
            nonlocal result, n
            for c in range(n):
                dv = (c - r + self.n - 1)
                adv = c + r
                if dv not in d and adv not in ad and c not in v:
                    if r == self.n - 1:
                        result += 1
                    else:
                        v.append(c), d.add(dv), ad.add(adv)
                        solve(r + 1, v, d, ad)
                        del v[-1]
                        d.remove(dv), ad.remove(adv)

        solve(0, [], set(), set())

        return result
