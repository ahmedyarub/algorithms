class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        mp, queue = defaultdict(list), [(root, 0)]

        while queue:
            node, col = queue.pop(0)

            if not node:
                continue

            mp[col].append(node.val)

            queue.append((node.left, col - 1))
            queue.append((node.right, col + 1))

        return [mp[col] for col in range(min(mp.keys()), max(mp.keys()) + 1)]
