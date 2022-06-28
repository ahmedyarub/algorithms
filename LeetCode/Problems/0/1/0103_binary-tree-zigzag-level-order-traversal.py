class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result, queue, level, cur_level = [], [(root, 0)], [], 0

        while queue:
            node, nl = queue.pop(0)

            if nl > cur_level:
                result.append(level[::-1 if cur_level % 2 else 1])
                level = []
                cur_level = nl

            level.append(node.val)

            if node.left:
                queue.append((node.left, nl + 1))
            if node.right:
                queue.append((node.right, nl + 1))

        return result + [level[::-1 if cur_level % 2 else 1]]
