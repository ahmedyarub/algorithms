class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def driver(cur: Optional[TreeNode]):
            if cur:
                cur.left, cur.right = cur.right, cur.left

                driver(cur.left)
                driver(cur.right)

        driver(root)

        return root
