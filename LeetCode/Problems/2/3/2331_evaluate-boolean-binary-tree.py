class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        if not root.val:
            return False

        if root.val == 3:
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)
        else:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
