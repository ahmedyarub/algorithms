class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        m = {}
        for i, s in enumerate(sorted(score, reverse=True)):
            if i == 0:
                m[s] = "Gold Medal"
            elif i == 1:
                m[s] = "Silver Medal"
            elif i == 2:
                m[s] = "Bronze Medal"
            else:
                m[s] = str(i + 1)

        return list(map(m.get, score))
