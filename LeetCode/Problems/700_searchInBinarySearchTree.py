class Solution(object):
    def searchBST(self, root, val):
        if root.val == val:
            return root
        elif root.val > val and root.left is not None:
            return self.searchBST(root.left, val)
        elif root.val < val and root.right is not None:
            return self.searchBST(root.right, val)

        return None
