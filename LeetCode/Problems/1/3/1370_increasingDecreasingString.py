class Solution:
    def sortString(self, s: str) -> str:
        d = sorted([c, n] for c, n in Counter(s).items())
        r = []
        while len(r) < len(s):
            for i in range(len(d)):
                if d[i][1]:
                    r.append(d[i][0])
                    d[i][1] -= 1
            for i in range(len(d)):
                if d[~i][1]:
                    r.append(d[~i][0])
                    d[~i][1] -= 1
        return ''.join(r)
