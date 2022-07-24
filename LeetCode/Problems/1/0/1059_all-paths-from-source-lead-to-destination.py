class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        mp = defaultdict(list)

        for v1, v2 in edges:
            mp[v1].append(v2)

        seen = set()

        @cache
        def traverse(node: int) -> bool:
            if node == destination and not mp[node]:
                return True

            if node in seen:
                return False

            seen.add(node)
            found = len(mp[node]) > 0 and all([traverse(to) for to in mp[node]])
            seen.remove(node)
            return found

        return traverse(source)
