class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:

        def longest_path(root: TreeNode) -> tuple[int, int]:
            nonlocal result

            if not root:
                return 0, 0

            inr = dcr = 1
            if root.left:
                left = longest_path(root.left)
                if root.val == root.left.val + 1:
                    dcr = left[1] + 1
                elif root.val == root.left.val - 1:
                    inr = left[0] + 1

            if root.right:
                right = longest_path(root.right)
                if root.val == root.right.val + 1:
                    dcr = max(dcr, right[1] + 1)
                elif root.val == root.right.val - 1:
                    inr = max(inr, right[0] + 1)

            result = max(result, dcr + inr - 1)
            return inr, dcr

        result = 0
        longest_path(root)
        return result
