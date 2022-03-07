class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        known = set()
        stack = [root]

        while stack:
            cur_node = stack.pop()

            if (k - cur_node.val) in known:
                return True

            known.add(cur_node.val)

            if cur_node.left:
                stack.append(cur_node.left)

            if cur_node.right:
                stack.append(cur_node.right)

        return False
