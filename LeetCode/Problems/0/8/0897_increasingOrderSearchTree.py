class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.last_node = result = TreeNode(None)

        def traverse(node):
            if node:
                traverse(node.left)
                node.left = None
                self.last_node.right = node
                self.last_node = node
                traverse(node.right)

        traverse(root)

        return result.right
