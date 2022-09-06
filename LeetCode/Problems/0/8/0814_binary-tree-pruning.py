class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: TreeNode) -> bool:
            one = False
            if node.left:
                if not dfs(node.left):
                    node.left = None
                else:
                    one = True

            if node.right:
                if not dfs(node.right):
                    node.right = None
                else:
                    one = True

            return one or node.val

        if not dfs(root):
            return None
        else:
            return root
