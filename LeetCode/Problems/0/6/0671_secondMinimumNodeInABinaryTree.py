class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.result = -1

        def findMinExcept(node, ex):
            if not node:
                return float('inf')

            if node.val != ex:
                if self.result == -1 or node.val < self.result:
                    self.result = node.val
                return

            findMinExcept(node.left, ex)
            findMinExcept(node.right, ex)

        findMinExcept(root, root.val)

        return self.result
