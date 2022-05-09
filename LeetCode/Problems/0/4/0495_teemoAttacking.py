class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        result = 0
        timeSeries.append(float('inf'))

        for i in range(len(timeSeries) - 1):
            result += min(duration, timeSeries[i + 1] - timeSeries[i])

        return result
