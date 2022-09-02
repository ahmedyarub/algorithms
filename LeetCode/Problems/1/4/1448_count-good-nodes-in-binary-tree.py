class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0

        def dfs(node: Optional[TreeNode], prev_max: int):
            nonlocal result

            if not node:
                return

            if prev_max <= node.val:
                result += 1
                prev_max = node.val

            dfs(node.left, prev_max)
            dfs(node.right, prev_max)

        dfs(root, float('-inf'))

        return result
