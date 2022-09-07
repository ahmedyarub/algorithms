class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], col: int, row: int) -> Tuple:
            if not node:
                return float('inf'), float('-inf'), float('-inf')

            lc, lr, lv = dfs(node.left, col - 1, row + 1)
            rc, rr, rv = dfs(node.right, col + 1, row + 1)

            if lr == float('-inf') and rr == float('-inf'):
                return col, row, node.val

            if lr == rr:
                if lc < rc:
                    return lc, lr, lv
                else:
                    return rc, rr, rv
            elif lr > rr:
                return lc, lr, lv
            else:
                return rc, rr, rv

        return dfs(root, 0, 0)[2]
