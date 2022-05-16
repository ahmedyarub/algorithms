class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def traverse(node, leafs):
            if not (node.left or node.right):
                leafs.append(node.val)

            if node.left:
                traverse(node.left, leafs)

            if node.right:
                traverse(node.right, leafs)

            return leafs

        return traverse(root1, []) == traverse(root2, [])
