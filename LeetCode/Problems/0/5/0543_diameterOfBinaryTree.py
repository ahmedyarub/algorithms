class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def getMaxDepth(node):
            if not node:
                return 0
            nonlocal diameter

            left_path = getMaxDepth(node.left)
            right_path = getMaxDepth(node.right)

            diameter = max(diameter, left_path + right_path)

            return max(left_path, right_path) + 1

        getMaxDepth(root)

        return diameter
