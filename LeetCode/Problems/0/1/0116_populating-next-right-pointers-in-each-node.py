class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        result, queue, level, cur_level = [], [(root, 0)], [], 0

        while queue:
            node, nl = queue.pop(0)

            if queue and queue[0][1] == nl:
                node.next = queue[0][0]

            if nl > cur_level:
                result.append(level)
                level = []
                cur_level = nl

            level.append(node.val)

            if node.left:
                queue.append((node.left, nl + 1))
            if node.right:
                queue.append((node.right, nl + 1))

        return root
