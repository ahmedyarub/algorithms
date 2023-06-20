class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result, queue, cur_level, last_node = [], [[root.left, 1], [root.right, 1]] if root else [], 0, root

        while queue:
            node, node_level = queue.pop(0)

            if not node:
                continue

            if node_level != cur_level:
                result.append(last_node.val)
                cur_level = node_level

            last_node = node
            queue.extend([[node.left, node_level + 1], [node.right, node_level + 1]])

        if last_node:
            result.append(last_node.val)

        return result
