# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def traverse(node, num):
            if not node:
                return

            num = (num << 1) | node.val

            if not (node.left or node.right):
                self.result += num
                return

            traverse(node.left, num)
            traverse(node.right, num)

        self.result = 0
        traverse(root, 0)

        return self.result
