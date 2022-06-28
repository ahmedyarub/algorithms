class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = 0

        def traverse(node: Optional[TreeNode], curs: int):
            nonlocal result
            if not node:
                return

            curs = curs * 10 + node.val
            if not node.left and not node.right:
                result += curs

            traverse(node.left, curs)
            traverse(node.right, curs)

        traverse(root, 0)

        return result
