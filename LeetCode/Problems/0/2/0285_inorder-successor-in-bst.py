class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        successor = None

        while root:

            if p.val >= root.val:
                root = root.right
            else:
                successor = root
                root = root.left

        return successor
