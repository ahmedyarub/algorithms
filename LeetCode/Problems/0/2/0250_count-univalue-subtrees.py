class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        result = 0

        def dfs(node: TreeNode) -> bool:
            nonlocal result
            uni_value = True
            for nxt in [node.left, node.right]:
                if nxt:
                    if not dfs(nxt) or node.val != nxt.val:
                        uni_value = False

            result += uni_value
            return uni_value

        dfs(root)
        return result
