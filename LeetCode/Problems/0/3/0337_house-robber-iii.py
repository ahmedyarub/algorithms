class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> tuple:
            if not node:
                return 0, 0

            l1, l2 = dfs(node.left)
            r1, r2 = dfs(node.right)

            return node.val + l2 + r2, max(l1, l2) + max(r1, r2)

        return max(dfs(root))
