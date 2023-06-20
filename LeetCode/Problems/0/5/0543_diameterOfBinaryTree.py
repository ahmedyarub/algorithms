class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0

        def traverse(node: Optional[TreeNode]) -> int:
            nonlocal result

            if not node:
                return 0

            left, right = traverse(node.left), traverse(node.right)

            result = max(result, left + right)

            return max(left, right) + 1

        traverse(root)

        return result
