class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def traverse(node, val):
            if not node:
                return True

            return node.val == val and traverse(node.left, val) and traverse(node.right, val)

        return traverse(root, root.val)
