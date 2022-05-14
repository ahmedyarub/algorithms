class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        node_times, adj, q = [0] + [float("inf")] * n, defaultdict(list), [[0, k]]

        for u, v, w in times:
            adj[u].append((v, w))

        while q:
            cur_time, node = q.pop(0)
            if cur_time < node_times[node]:
                node_times[node] = cur_time

                for v, w in adj[node]:
                    q.append([cur_time + w, v])

        mx = max(node_times)
        return mx if mx < float("inf") else -1
