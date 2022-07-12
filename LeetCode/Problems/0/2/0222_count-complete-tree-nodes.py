class Solution:
    def countNodes(self, root):
        if not root:
            return 0
        left_depth = self.get_depth(root.left)
        right_depth = self.get_depth(root.right)
        if left_depth == right_depth:
            return pow(2, left_depth) + self.countNodes(root.right)
        else:
            return pow(2, right_depth) + self.countNodes(root.left)

    def get_depth(self, root):
        if not root:
            return 0
        return 1 + self.get_depth(root.left)
