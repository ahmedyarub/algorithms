class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        result, covered = 0, {None}

        def dfs(node, parent):
            nonlocal result

            if node:
                dfs(node.left, node)
                dfs(node.right, node)

                if node.left not in covered or node.right not in covered or (node not in covered and not parent):
                    result += 1
                    covered.update({node, node.left, node.right, parent})

        dfs(root, None)

        return result
