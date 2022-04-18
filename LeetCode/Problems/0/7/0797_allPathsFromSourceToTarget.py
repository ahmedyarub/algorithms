class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        queue = [[0]]
        n = len(graph)
        while queue:
            cur_path = queue.pop()

            for to_node in graph[cur_path[-1]]:
                new_path = cur_path + [to_node]
                if to_node == n - 1:
                    result.append(new_path)
                else:
                    queue.append(new_path)

        return result
