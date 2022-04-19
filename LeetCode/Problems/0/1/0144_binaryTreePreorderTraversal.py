class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.result = []

        def traverse(node):
            if not node:
                return

            self.result.append(node.val)

            traverse(node.left)
            traverse(node.right)

        traverse(root)

        return self.result
