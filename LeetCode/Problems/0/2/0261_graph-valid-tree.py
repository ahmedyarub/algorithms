class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        queue, cnt = [[0, 0]], 0

        while queue and cnt <= n:
            cur, prev = queue.pop(0)
            cnt += 1

            for edge in adj[cur]:
                if edge != prev:
                    queue.append([edge, cur])

        return cnt == n
