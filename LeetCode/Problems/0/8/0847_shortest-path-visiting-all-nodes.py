class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        if len(graph) == 1:
            return 0

        n = len(graph)
        ending_mask = (1 << n) - 1
        queue = [(node, 1 << node) for node in range(n)]
        seen = set(queue)

        steps = 0
        while queue:
            next_queue = []
            for i in range(len(queue)):
                node, mask = queue[i]
                for neighbor in graph[node]:
                    next_mask = mask | (1 << neighbor)
                    if next_mask == ending_mask:
                        return 1 + steps

                    if (neighbor, next_mask) not in seen:
                        seen.add((neighbor, next_mask))
                        next_queue.append((neighbor, next_mask))

            steps += 1
            queue = next_queue