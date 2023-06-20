class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        result = None

        def traverse(node: Optional[TreeNode]) -> List[int]:
            nonlocal result

            if result or not node:
                return 0

            cur = 1 if node.val == p.val or node.val == q.val else 0

            total_found = sum([cur, traverse(node.left), traverse(node.right)])

            if total_found == 2:
                result = node
                total_found = 0

            return total_found

        traverse(root)

        return result
