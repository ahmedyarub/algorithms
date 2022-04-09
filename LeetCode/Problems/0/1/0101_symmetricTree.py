class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def traverse(node1, node2):
            if not node1 and not node2:
                return True

            if not node1 or not node2:
                return False

            return node1.val == node2.val and \
                   traverse(node1.left, node2.right) and \
                   traverse(node1.right, node2.left)

        return traverse(root.left, root.right)
