class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        return [[pr[2] for pr in list(g)] for _, g in groupby(
            sorted([[len(st), reduce(lambda s, d: s * 26 + d,
                                     [(ord(st[i]) - ord(st[i - 1]) + 26) % 26 for i, c in enumerate(st[1:], 1)],
                                     0), st] for st in strings]), key=lambda sm_st: sm_st[0:2])]
