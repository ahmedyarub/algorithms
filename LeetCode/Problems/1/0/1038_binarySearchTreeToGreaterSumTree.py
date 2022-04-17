class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def traverse(node, start):
            if not node:
                return start

            node.val += traverse(node.right, start)
            return traverse(node.left, node.val)

        traverse(root, 0)

        return root
