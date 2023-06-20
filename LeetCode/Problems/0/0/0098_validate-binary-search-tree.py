class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        result = True

        def traverse(node: Optional[TreeNode]):
            nonlocal result
            if not result:
                return [float('-inf'), float('inf')]

            if node.left:
                left = traverse(node.left)
                mx_left = left[1]
                mn_left = left[0]
                if mx_left >= node.val:
                    result = False
            else:
                mn_left = node.val

            if node.right:
                right = traverse(node.right)
                mn_right = right[0]
                mx_right = right[1]
                if mn_right <= node.val:
                    result = False
            else:
                mx_right = node.val

            return [mn_left, mx_right]

        traverse(root)

        return result
