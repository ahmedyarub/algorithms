class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> tuple:
            if not node:
                return True, 0, float('inf'), float('-inf')

            lbst, lcnt, lmn, lmx = dfs(node.left)
            rbst, rcnt, rmn, rmx = dfs(node.right)

            if lbst and rbst and lmx < node.val and rmn > node.val:
                return True, lcnt + rcnt + 1, min(lmn, node.val), max(rmx, node.val)
            else:
                return False, max(lcnt, rcnt), None, None

        return dfs(root)[1]
