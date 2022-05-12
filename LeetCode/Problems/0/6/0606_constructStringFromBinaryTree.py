class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        s = [str(root.val)]

        if root.left:
            s.append("(" + self.tree2str(root.left) + ")")
        elif root.right:
            s.append("()")

        if root.right:
            s.append("(" + self.tree2str(root.right) + ")")

        return "".join(s)
