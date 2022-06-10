class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        nodes = set()

        for edge in edges:
            if edge[0] in nodes:
                return edge[0]
            nodes.add(edge[0])

            if edge[1] in nodes:
                return edge[1]
            nodes.add(edge[1])