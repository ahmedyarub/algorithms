class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def compareTrees(r1, r2):
            queue = [[r1, r2]]
            while queue:
                t1, t2 = queue.pop()

                if not t1 or not t2:
                    if t1 != t2:
                        return False

                    continue

                if t1.val != t2.val:
                    return False

                queue.append([t1.left, t2.left])
                queue.append([t1.right, t2.right])

            return True

        queue = [root]
        while queue:
            cur = queue.pop()

            if not cur:
                continue

            if cur.val == subRoot.val:
                if compareTrees(cur, subRoot):
                    return True

            queue.append(cur.left)
            queue.append(cur.right)

        return False
