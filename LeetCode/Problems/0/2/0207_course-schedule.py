class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mp = defaultdict(list)

        for p in prerequisites:
            mp[p[0]].append(p[1])

        def traverse(n: int, visited: set) -> bool:
            visited.add(n)

            for b in mp[n]:
                if b in visited or not traverse(b, visited):
                    return False

            visited.remove(n)
            del mp[n]

            return True

        return all([traverse(a, set()) for a, _ in prerequisites])
