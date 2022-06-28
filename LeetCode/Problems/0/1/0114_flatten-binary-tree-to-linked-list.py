class Solution:
    def flattenTree(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        if not node:
            return None

        if not node.left and not node.right:
            return node

        lt = self.flattenTree(node.left)
        rt = self.flattenTree(node.right)

        if lt:
            lt.right = node.right
            node.right = node.left
            node.left = None

        return rt if rt else lt

    def flatten(self, root: TreeNode) -> None:
        self.flattenTree(root)
