class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = [[root, 0, None]]
        other_depth = None
        other_parent = None
        while queue:
            node, depth, parent = queue.pop(0)

            if other_depth and depth != other_depth:
                return False

            if not node:
                continue

            if node.val == x or node.val == y:
                if other_depth == depth:
                    return other_parent != parent
                else:
                    other_depth = depth
                    other_parent = parent

            queue.append([node.left, depth + 1, node])
            queue.append([node.right, depth + 1, node])
