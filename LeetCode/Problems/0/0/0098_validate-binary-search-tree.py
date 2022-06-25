class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traverse(node: Optional[TreeNode], mn: int, mx: int) -> bool:
            return not node \
                   or (mn < node.val < mx and traverse(node.left, mn, node.val) and traverse(node.right, node.val, mx))

        return traverse(root, float('-inf'), float('inf'))
