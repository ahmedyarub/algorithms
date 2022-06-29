class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        seen = dict()

        def clone(node: 'Node') -> 'Node':
            nonlocal seen
            if node.val in seen:
                return seen[node.val]

            new_node = Node(node.val)
            seen[node.val] = new_node

            for neighbor in node.neighbors:
                new_node.neighbors.append(clone(neighbor))

            return new_node

        return clone(node)
