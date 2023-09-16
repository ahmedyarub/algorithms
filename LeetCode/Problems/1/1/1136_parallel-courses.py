class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        incoming, result, adj = defaultdict(int), -1, defaultdict(list)

        for frm, to in relations:
            incoming[to] += 1
            adj[frm].append(to)

        queue = deque((node, 1) for node in range(1, n + 1) if not incoming[node])

        while queue:
            node, layer = queue.popleft()
            result = max(result, layer)

            for to in adj[node]:
                incoming[to] -= 1
                if not incoming[to]:
                    queue.append((to, layer + 1))

        return -1 if any(incoming.values()) else result
