class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cur_k, result = 0, 0

        def get_smallest(node: TreeNode):
            nonlocal cur_k, k, result
            if result:
                return

            if node.left:
                get_smallest(node.left)

            cur_k += 1

            if cur_k == k:
                result = node.val
                return

            if node.right:
                get_smallest(node.right)

        get_smallest(root)

        return result
