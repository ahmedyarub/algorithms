class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        visited, queue = set(), [(0, None)]
        while queue:
            node, parent = queue.pop()
            if node in visited:
                return False

            visited.add(node)
            queue.extend([(nxt, node) for nxt in adj[node] if nxt != parent])
            del adj[node]

        return len(visited) == n
