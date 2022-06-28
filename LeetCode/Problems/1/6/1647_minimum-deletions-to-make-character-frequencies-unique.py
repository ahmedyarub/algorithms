class Solution:
    def minDeletions(self, s: str) -> int:
        counts = {cnt: cntcnt for cnt, cntcnt in Counter(Counter(list(s)).values()).items()}
        targets = [cnt for cnt, cntcnt in counts.items() if cntcnt > 1]

        result = 0

        for cnt in targets:
            while counts[cnt] > 1:
                newcnt = cnt
                while newcnt and newcnt in counts:
                    result += 1
                    newcnt -= 1

                counts[newcnt] = 1
                counts[cnt] -= 1

        return result
