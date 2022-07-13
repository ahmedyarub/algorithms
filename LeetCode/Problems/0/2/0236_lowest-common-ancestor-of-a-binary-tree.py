class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        result = None

        def find(node: TreeNode) -> bool:
            nonlocal result
            if not node:
                return False

            if node == p or node == q:
                if find(node.left) or find(node.right):
                    result = node

                return True

            l, r = find(node.left), find(node.right)
            if l and r and not result:
                result = node
                return False
            else:
                return l or r

        find(root)
        return result
