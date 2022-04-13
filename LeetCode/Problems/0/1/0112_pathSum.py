class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        targetSum -= root.val

        if not (root.left or root.right):
            return not targetSum

        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
