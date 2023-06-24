class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        jobs = sorted([(startTime[i], endTime[i], profit[i]) for i in range(len(startTime))])
        heap = []
        cp, mp = 0, 0
        for s, e, p in jobs:
            while heap and heap[0][0] <= s:
                et, tmp = heappop(heap)
                cp = max(cp, tmp)
            heappush(heap, (e, cp + p))
            mp = max(mp, cp + p)

        return mp
