class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.arr = []

        def scan(cur_node):
            if cur_node.left:
                scan(cur_node.left)

            self.arr.append(cur_node.val)

            if cur_node.right:
                scan(cur_node.right)

        scan(root)

        min_dif = float('inf')

        for i in range(len(self.arr) - 1):
            min_dif = min(min_dif, abs(self.arr[i + 1] - self.arr[i]))

        return min_dif
