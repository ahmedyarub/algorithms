class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        mp, result = defaultdict(list), []

        for ticket in tickets:
            mp[ticket[0]].append(ticket[1])

        for destinations in mp.values():
            destinations.sort(reverse=True)

        def dfs(airport: str) -> None:
            destinations = mp[airport]

            while destinations:
                nxt = destinations.pop()
                dfs(nxt)

            result.append(airport)

        dfs("JFK")

        result.reverse()

        return result
