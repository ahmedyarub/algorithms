class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        result = True

        def driver(node: Optional[TreeNode]) -> int:
            nonlocal result

            if not node:
                return 0

            left = driver(node.left)
            right = driver(node.right)

            if abs(right - left) > 1:
                result = False

            return max(left, right) + 1

        driver(root)

        return result
