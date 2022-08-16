class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        sarr = sorted([(p[0], i) for i, p in enumerate(intervals)])
        earr = sorted([(p[1], i) for i, p in enumerate(intervals)])
        result, si = [], 0

        for end, ei in earr:
            while si < len(sarr) and sarr[si][0] < end:
                si += 1

            if si == len(sarr):
                result.append((ei, -1))
            else:
                result.append((ei, sarr[si][1]))

        return list(map(lambda pair: pair[1], sorted(result)))
