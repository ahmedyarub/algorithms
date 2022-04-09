class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True

        def traverse(node):
            if not self.balanced or not node:
                return 0

            left = traverse(node.left)
            right = traverse(node.right)

            if abs(left - right) > 1:
                self.balanced = False

            return max(left, right) + 1

        traverse(root)

        return self.balanced
