class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        result = 1

        def dfs(node: Optional[TreeNode], depth: int, prev: int):
            nonlocal result
            if not node:
                return
            if node.val - 1 == prev:
                depth += 1
                result = max(result, depth)
            else:
                depth = 1
            dfs(node.left, depth, node.val)
            dfs(node.right, depth, node.val)

        dfs(root, 1, float('-inf'))

        return result
