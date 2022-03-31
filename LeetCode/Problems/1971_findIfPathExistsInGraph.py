class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        adj_mat = defaultdict(list)

        for u, v in edges:
            adj_mat[u].append(v)
            adj_mat[v].append(u)

        queue = [source]

        while queue:
            u = queue.pop()

            vs = adj_mat[u]

            for v in vs:
                if v == destination:
                    return True

                queue.append(v)

            del adj_mat[u]

        return False
