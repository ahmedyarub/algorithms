class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        arr = []

        def inorder(node: Optional[TreeNode]) -> None:
            if node:
                inorder(node.left)
                arr.append(node)
                inorder(node.right)

        inorder(root)

        wrong = []
        for i, node in enumerate(arr):
            if (i > 0 and node.val < arr[i - 1].val) or (i < len(arr) - 1 and node.val > arr[i + 1].val):
                wrong.append(node)

        wrong[0].val, wrong[-1].val = wrong[-1].val, wrong[0].val
