class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dict, finishable = defaultdict(list), [n for n in range(numCourses)]

        for prerequisite in prerequisites:
            dict[prerequisite[0]].append(prerequisite[1])
            if prerequisite[0] in finishable:
                finishable.remove(prerequisite[0])

        for prerequisite in prerequisites:
            known = set()

            def traverse(node: int) -> bool:
                nonlocal known, finishable
                if node in finishable:
                    return True

                if node in known:
                    return False
                else:
                    known.add(node)
                if all([traverse(next_node) for next_node in dict[node]]) if node in dict else True:
                    known.remove(node)
                    finishable.append(node)
                    return True
                else:
                    return False

            if not traverse(prerequisite[0]):
                return False

        return True
