class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.result = 0

        def traverse(node):
            if not node:
                return 0

            left, right = traverse(node.left), traverse(node.right)
            self.result += abs(left - right)

            return node.val + left + right

        traverse(root)

        return self.result
