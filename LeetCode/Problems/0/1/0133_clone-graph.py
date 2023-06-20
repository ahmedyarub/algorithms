class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        known = {}

        def driver(node: 'Node') -> 'Node':
            nonlocal known

            if node:
                if node in known:
                    return known[node]

                newNode = Node(node.val, [])
                known[node] = newNode

                newNode.neighbors = [driver(neighbor) for neighbor in node.neighbors]

                return newNode

        return driver(node)
