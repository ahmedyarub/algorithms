class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        if not root.left and not root.right:
            return root

        nr = self.upsideDownBinaryTree(root.left)
        self.upsideDownBinaryTree(root.right)

        if nr is None:
            nr = root.left
        root.left.left, root.left.right, root.left, root.right = root.right, root, None, None

        return nr
