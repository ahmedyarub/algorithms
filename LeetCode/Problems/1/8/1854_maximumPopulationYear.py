class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        delta = [0] * 101

        conversionDiff = 1950

        for l in logs:
            delta[l[0] - conversionDiff] += 1
            delta[l[1] - conversionDiff] -= 1

        runningSum = 0
        maxPop = 0
        year = 1950

        for i, d in enumerate(delta):
            runningSum += d

            if runningSum > maxPop:
                maxPop = runningSum
                year = conversionDiff + i

        return year
