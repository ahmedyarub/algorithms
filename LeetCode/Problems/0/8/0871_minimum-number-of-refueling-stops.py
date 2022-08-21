class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        pq = []
        stations.append([target, float('inf')])

        ans = prev = 0
        for location, capacity in stations:
            startFuel -= location - prev
            while pq and startFuel < 0:  # must refuel in past
                startFuel += -heappop(pq)
                ans += 1

            if startFuel < 0:
                return -1
            heappush(pq, -capacity)
            prev = location

        return ans
