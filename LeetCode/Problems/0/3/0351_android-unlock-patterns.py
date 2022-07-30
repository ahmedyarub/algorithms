class Solution:
    def numberOfPatterns(self, m, n, patterns=None):
        if patterns is None:
            patterns = []

        bad = re.compile('[^2]*(13|31)|[^4]*(17|71)|[^8]*(79|97)|[^6]*(39|93)|[^5]*(19|28|37|46|64|73|82|91)').match

        while len(patterns) <= n:
            patterns += sum(not bad(''.join(p)) for p in permutations('123456789', len(patterns))),
        return sum(patterns[m:n + 1])
