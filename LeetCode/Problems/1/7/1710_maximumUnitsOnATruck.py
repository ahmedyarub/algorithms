class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        result = 0

        for nb, nub in sorted(boxTypes, reverse=True, key=lambda bt: bt[1]):
            b = min(nb, truckSize)
            result += (b * nub)
            truckSize -= b

            if not truckSize:
                break

        return result
