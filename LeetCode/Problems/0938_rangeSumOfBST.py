class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        s = 0

        if high >= root.val >= low:
            s += root.val

        if root.val > low:
            s += self.rangeSumBST(root.left, low, high)

        if root.val < high:
            s += self.rangeSumBST(root.right, low, high)

        return s
