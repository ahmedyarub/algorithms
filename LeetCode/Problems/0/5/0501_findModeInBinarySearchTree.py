class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counts = defaultdict(int)
        self.max_count = 0

        def traverse(node):
            if not node:
                return

            counts[node.val] += 1
            self.max_count = max(self.max_count, counts[node.val])

            traverse(node.left)
            traverse(node.right)

        traverse(root)

        return [v for v, c in counts.vehicles() if c == self.max_count]
