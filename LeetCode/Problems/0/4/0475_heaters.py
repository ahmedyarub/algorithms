class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        result, pos, heaters = 0, 0, [float('-inf')] + heaters + [float('inf')]
        for house in houses:
            while house >= heaters[pos]:
                pos += 1
            r = min(house - heaters[pos - 1], heaters[pos] - house)
            result = max(result, r)

        return result
