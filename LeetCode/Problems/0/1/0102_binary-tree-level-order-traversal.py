class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result, queue, level, cur_level = [], [(root, 0)], [], 0

        while queue:
            node, nl = queue.pop(0)

            if nl > cur_level:
                result.append(level)
                level = []
                cur_level = nl

            level.append(node.val)

            if node.left:
                queue.append((node.left, nl + 1))
            if node.right:
                queue.append((node.right, nl + 1))

        return result + [level]
