class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.heap = []
        self.buildHeap(root)

        for _ in range(k - 1):
            heappop(self.heap)

        return heappop(self.heap)

    def buildHeap(self, node):
        if node is None:
            return

        heappush(self.heap, node.val)
        self.buildHeap(node.left)
        self.buildHeap(node.right)
