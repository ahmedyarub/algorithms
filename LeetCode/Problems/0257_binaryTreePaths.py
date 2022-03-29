class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:
                    result.append(path)
                else:
                    path += '->'
                    dfs(root.left, path)
                    dfs(root.right, path)

        result = []

        dfs(root, '')

        return result
