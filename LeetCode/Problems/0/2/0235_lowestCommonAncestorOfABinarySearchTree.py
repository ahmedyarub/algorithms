class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        queue = [root]

        if p.val > q.val:
            p, q = q, p

        while queue:
            node = queue.pop()

            if node:
                if p == node or q == node or p.val < node.val < q.val:
                    return node

                queue.append(node.left)
                queue.append(node.right)
