class Solution:
    def findCelebrity(self, n: int) -> int:
        cand = 0
        for i in range(1, n):
            if knows(cand, i):
                cand = i

        return cand if all(not knows(cand, x) for x in range(cand)) \
                       and all(knows(x, cand) for x in range(n) if x != cand) \
            else -1
