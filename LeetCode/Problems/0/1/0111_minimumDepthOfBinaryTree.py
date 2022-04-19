class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        queue = [[root, 1]]

        while queue:
            node, depth = queue.pop(0)
            if not node:
                continue

            if not node.left and not node.right:
                return depth

            queue.append([node.left, depth + 1])
            queue.append([node.right, depth + 1])

        return 0
