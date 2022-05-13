class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        queue = [[root, 0]]

        while queue:
            node, level = queue.pop(0)

            if queue and queue[0][1] == level:
                node.next = queue[0][0]

            if node.left:
                queue.append([node.left, level + 1])

            if node.right:
                queue.append([node.right, level + 1])

        return root
