class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result, indegree, rmp = [], defaultdict(int), defaultdict(set)

        for a, b in prerequisites:
            indegree[a] += 1
            rmp[b].add(a)

        queue = [n for n in range(numCourses) if not indegree[n]]

        while queue:
            b = queue.pop()
            result.append(b)

            for a in rmp[b]:
                indegree[a] -= 1
                if not indegree[a]:
                    queue.append(a)

        return [] if len(result) < numCourses else result
