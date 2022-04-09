class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = [[p, q]]

        while queue:
            cur_p, cur_q = queue.pop()

            if not cur_p and not cur_q:
                continue

            if not cur_q or not cur_p or cur_p.val != cur_q.val:
                return False

            queue.append([cur_p.left, cur_q.left])
            queue.append([cur_p.right, cur_q.right])

        return True
