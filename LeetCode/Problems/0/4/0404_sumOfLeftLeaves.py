class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def calc(node, left):
            if not node:
                return 0

            if not (node.left or node.right):
                return node.val if left else 0

            return calc(node.left, True) + calc(node.right, False)

        return calc(root, False)
