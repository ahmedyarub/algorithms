class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        f = s = 0
        ans = []

        while f != len(firstList) and s != len(secondList):
            start = max(firstList[f][0], secondList[s][0])
            end = min(firstList[f][1], secondList[s][1])

            if s == len(secondList) or firstList[f][1] <= end:
                f += 1

            if f == len(firstList) or secondList[s][1] <= end:
                s += 1

            if end >= start:
                ans.append([start, end])

        return ans
