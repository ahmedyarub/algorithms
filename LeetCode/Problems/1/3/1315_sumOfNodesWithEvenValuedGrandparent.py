class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.result = 0

        def traverse(node, p, g):
            if not node:
                return

            if not g % 2:
                self.result += node.val

            traverse(node.left, node.val, p)
            traverse(node.right, node.val, p)

        traverse(root, 1, 1)

        return self.result
