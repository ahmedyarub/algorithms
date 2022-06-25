class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        all_points, adj = set(range(n)), defaultdict(list)

        for frm, to in edges:
            adj[frm].append(to)
            adj[to].append(frm)

        result, groups = 0, 0
        while all_points:
            group = 1
            queue = [all_points.pop()]

            while queue:
                cur = queue.pop()

                for to in adj[cur]:
                    if to in all_points:
                        queue.append(to)
                        all_points.remove(to)
                        group += 1

                del adj[cur]

            result += groups * group
            groups += group

        return result
