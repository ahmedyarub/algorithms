class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(defaultdict)

        def dfs(numer: int, denom: int, prev: float, vis: set) -> float:
            vis.add(numer)
            res = -1.0

            neighbors = adj[numer]

            if denom in neighbors:
                res = prev * adj[numer][denom]
            else:
                for neighbor, v in neighbors.items():
                    if neighbor not in visited:
                        res = dfs(neighbor, denom, prev * v, vis)

                        if res != -1.0:
                            break

            vis.remove(numer)
            return res

        for v, (numer, denom) in zip(values, equations):
            adj[numer][denom] = v
            adj[denom][numer] = 1 / v

        result = []

        for numer, denom in queries:
            if numer not in adj or denom not in adj:
                result.append(-1.0)
            elif numer == denom:
                result.append(1)
            else:
                visited = set()
                result.append(dfs(numer, denom, 1, visited))

        return result
